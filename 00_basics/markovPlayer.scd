// start server
s.boot;

// verify port
NetAddr.langPort

(
// python server is listening on port 57310
b = NetAddr("127.0.0.1", 57310);

// our function to send a message to python
~startCalc = {|audioPath, grainSize, hopSize|
	b.sendMsg("/start_calc", audioPath, grainSize, hopSize);
};

// will store our shared data
q = ();
// empty matrix P
q[\P] = [[1]];
// default buffer
q[\buffer] = Buffer.read(s, Platform.resourceDir +/+ "sounds/a11wlk01.wav");
q[\grainSize] = 44100;
q[\hopSize] = 4000;

// our callback function in which we parse the results from python
OSCdef(\calcFinished, {|msg|
	var json = msg[1].asString.parseYAMLFile;
	q[\P] = json["P"].asFloat;
	q[\buffer] = Buffer.read(s, json["audioPath"]);
	q[\grainSize] = json["grainSize"].asFloat;
	q[\hopSize] = json["hopSize"].asFloat;
	"Switched out data".postln;
}, "/calc_finished");

// a synthdef which can play a section of a buffer
SynthDef(\bplaySection, {|out|
	var bufNum = \bufnum.kr(0);
	var start = \start.kr(0);
    var env = EnvGen.kr(Env.linen(
		attackTime: \attack.kr(0.001),
		sustainTime: (\end.kr(1000)-start)/BufSampleRate.kr(bufNum),
		releaseTime: \release.kr(0.001),
    ), doneAction: Done.freeSelf);
    var sig = PlayBuf.ar(
        numChannels: 2,
		bufnum: bufNum,
		rate: BufRateScale.kr(bufNum) * \rate.kr(1.0),
		startPos: start,
    );
	sig = sig*env*\amp.kr(0.5);
    Out.ar(out, sig);
}).add;

// a tdef which will playback the buffer according to our markov transition matrix P
Tdef(\playMarkov, {
    var curState=0;
	loop {
		// calculate next state which aka the next grain
		curState = (0..q[\P].shape[0]).wchoose(q[\P][curState].normalizeSum);
        // playback
		Synth(\bplaySection, [
			\bufnum, q[\buffer].bufnum,
		    \start, curState*q[\hopSize],
	     	\end, curState*q[\hopSize] + q[\grainSize],
            \amp, 0.5,
            \attack, 0.1,
        ]);
		// by reducing the factor of our wait time
		// the played back samples will overlap more
		((q[\grainSize]/s.sampleRate)*0.5).wait;
    };
}).play;
)

// now we can change parameters from within supercollider
(
~startCalc.(
	// use absolute paths
	// the example is mono and we build for stereo so we will get some problems
	audioPath: Platform.resourceDir +/+ "sounds/a11wlk01.wav",
	grainSize: 10000,
	// pay attention when reducing hop size
	// as the calculated data grows exponentially
	// because we obtain more grains and for each
	// grain we calulate the distance to all other
	// grains
	hopSize: 1000,
)
)