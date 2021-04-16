Math basics
===========

In this document we want to explore the most fundamental mathematical concepts which are needed
for the basics of machine learning.
This guide can not even scratch the surface of the tremendous amount of topics which should be covered but we can try nonetheless.

We will also discuss the notion that is used throughout the course.

A recommended read for a quick introduction is :cite:p:`2019:burkov`.

Data structures
---------------

We define a *scalar* :math:`x` as a single numerical value and we note it as a single lowercase letter.
Examples for a *scalar* can be a whole number like :math:`2` or a real number like :math:`0.25`.

A *vector* :math:`\text{x}` is a list of :math:`n` *scalar* values with a fixed ordering of this collection.
We call this an *n-dimensional vector*.
For example :math:`\text{a} = [3, 2]` is a 2-dimensional vector.
We denote the :math:`i`-th value of a vector :math:`\text{x}` via :math:`x^{(i)}`, so in our example :math:`a^{(1)} = 3`.
This index also denotes the dimension of a vector.

A :math:`n \times m` *matrix* :math:`\text{A}` is an collection of numerical values which consists of :math:`m` *rows* and :math:`n` *columns*.
The values of such are matrix are arranged as

.. math::

    \text{A} =
    \begin{pmatrix}
       a_{1,1} & \cdots & a_{1,n} \\
       \vdots & \ddots & \vdots \\
       a_{m,1} & \cdots & a_{m,n}
    \end{pmatrix}


A *set* :math:`\mathcal{S}` is a collection of unique elements, so e.g. :math:`\mathcal{A} = \lbrace 5, 4 , 20 \rbrace` or :math:`\mathcal{B} = \lbrace x_1, x_2, \dots, x_{n} \rbrace`.
Common sets are the set of all real numbers :math:`\mathbb{R}` or the set of all natural numbers :math:`\mathbb{N}`.
We call a set of vectors a *vector set*.

We denote :math:`b` is an element of a set :math:`\mathcal{B}` by writing :math:`b \in \mathcal{B}` or in the opposite when an element :math:`c` is not
contained in the set :math:`\mathcal{B}` by writing :math:`c \notin \mathcal{B}`.

We denote the *cardinality* of a set :math:`\mathcal{S}` as :math:`|\mathcal{S}|` defined as the number of elements in the set :math:`\mathcal{S}`, so with our
examples from above we have :math:`|\mathcal{A}| = 3` and :math:`|\mathcal{B}| = n`. 

The cardinality of a set can either be finite (such as :math:`\mathcal{A}` and :math:`\mathcal{B}`) but they can also contain an infinite amount of elements
such as :math:`\mathbb{R}`.

Suppose we have two elements :math:`a` and :math:`b`.
If a set includes everything between :math:`a` and :math:`b` and also :math:`a` and :math:`b` itself we define it as a *closed interval* which is denoted as :math:`[a,b]`.
If :math:`a` and :math:`b` are not included in this set we define it as an *open interval* denoted as :math:`(a,b)`.

Functions
---------

A *function* :math:`f: \mathcal{X} \rightarrow \mathcal{Y}` transfers each element :math:`x \in \mathcal{X}` to a single element :math:`y \in \mathcal{Y}` where :math:`\mathcal{X}` is
defined as the *domain* of a function and :math:`\mathcal{Y}` as the *co-domain*.
We often use the notation :math:`y = f(x)`.
An example for this would be :math:`f: \mathbb{Z} \rightarrow \mathbb{N}` which is defined by :math:`f(x) := x+4` where :math:`\mathbb{Z}` is the
set of all rational numbers and we use :math:`:=` to say that something is defined by the equation.

Of course domain and co-domain can be the same such as in :math:`g: \mathbb{R} \rightarrow \mathbb{R}` which is defined by :math:`g(x):= x^2`.
We see that the notion of the domain and co-domain is quite important and also allows us to shift between dimensions, e.g. the
*euclidian metric* :math:`d(p,q) = ||p-q||_{2}` of two vectors :math:`p, q \in \mathbb{R}^n` is defined as

.. math::

    d(p,q) = ||p-q||_{2} := \sqrt{(q_1 - p_1)^2 + \dots + (q_n - p_n)^2 } = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2 }

so :math:`d: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}_{\geq 0}`.
Although we provide high dimensions as input for our function we will receive a single scalar value as output of the equation.
The euclidian metric is an instance of a *metric* which defines a distance between two points in a vector space and therefore has to `meet certain criteria <https://en.wikipedia.org/wiki/Metric_(mathematics)#Definition>`_.
A metric will be a crucial guideline for us when we are working in high, non-imaginable dimensions.

We define the *local minimum* of a function :math:`f: \mathcal{X} \rightarrow \mathcal{Y}` at a point :math:`c \in \mathcal{X}` if :math:`f(x) \gt f(c)` for every
:math:`x` in an open interval around :math:`c`.
The minimum value across all local minima is defined as the *global minimum*.
This will be another crucial point of this course as this is `a research field on its own <https://en.wikipedia.org/wiki/Optimization_problem>`__.
Much of machine learning is tied to the riddle of finding the best solution to a problem - e.g. finding the lowest cost.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/1/1e/Extrema_example.svg
    :alt: Global and local maximum/minimum

    Example of a global and local minimum/maximum.
    `Source <https://commons.wikimedia.org/wiki/File:Extrema_example.svg>`__

Looking at this graph it seems quiet obvious to find the minimum and maximum - but when we working in non-imaginary and viewable dimensions
we can not take a look at it.
Also in order to take a look at a graph we need to calculate every point of it which can get quite tricky at higher dimensions.

Before taking a look at `the problem of higher dimensions <https://en.wikipedia.org/wiki/Curse_of_dimensionality>`__ we want to define
a way no how to calculate the local and global minimum.

The *derivative* :math:`f'` of a function :math:`f` is a function which describes the growth and decrease of the function :math:`f`.
A function :math:`f: \mathcal{A} \rightarrow \mathcal{B}` is derivable at a point :math:`a \in \mathcal{A}` if

.. math::

    \lim_{x \rightarrow x_0} = \frac{f(x) - f(x_0)}{x-x_0}

exists.
If we replace :math:`x` with :math:`x_0+h` we obtain

.. math::

    \lim_{h \rightarrow 0} = \frac{f(x_0 + h) - f(x_0)}{h} := f'(x_0)

which describes the derivative of :math:`f` at the point :math:`x_0`.
Understanding the meaning of this is not trivial but basically it limits the growth of a function within a region.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/c/cc/Tangent_animation.gif
    :alt: Calculation of the tangent

    By approaching :math:`\Delta x \rightarrow 0` we obtain a tangent which describes the growth
    at the point :math:`x`.
    `Source <https://commons.wikimedia.org/wiki/File:Tangent_animation.gif>`__

The derivative of the basic function :math:`f: \mathbb{R} \rightarrow \mathbb{R}` for :math:`f(x)=x^2` is :math:`f'(x)=2x`.
The *second order derivative* :math:`f''` is defined as the derivative of the derivative - in our example it is
:math:`f''=2` and :math:`f''' = f^{(3)} = 0`.
The reverse procedure of derivation is called *integration* of a function.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/6/6b/Absolute_value.svg
    :alt: Plot of :math:`f(x) = |x|`.

    Not every function is differentable. E.g. :math:`f: \mathbb{R} \rightarrow \mathbb{R}` with :math:`f(x)=|x|` is not 
    differentable at :math:`x=0`.
    This will become important when working with neural networks.
    `Source <https://commons.wikimedia.org/wiki/File:Absolute_value.svg>`__

Working with vectors and matrices
---------------------------------

After we have defined vectors and matrices in :ref:`Data structures` we also want to take a look at how to work with them.

The *sum* of two vectors :math:`\text{a},\text{b}` is defined by

.. math::

    \text{a} + \text{b} = [a_1 + b_1, a_2 + b_2, \dots, a_m + b_m]

We see that this definition can only be applied if the dimensions of both vectors match.
If they do not match the addition of 2 vectors is not defined.

We can *scale* our vector :math:`\text{a}` by *multiplying a scalar* :math:`c` to it which is defined by

.. math::

    c\text{a} = [ca_1, ca_2, ..., cx_m]

The *dot product* :math:`\cdot` of two vectors :math:`\text{a}, \text{b}` is given by

.. math::

    \text{a} \cdot \text{b} = \sum_{i=1}^{m} a_i b_i

which returns a scalar.
Once again this is only defined if both dimensions match.

The addition of two :math:`m \times n` matrices :math:`\text{A},\text{B}` is defined as

.. math::

    \text{A} + \text{B} =
    \begin{pmatrix}
       a_{1,1} & \cdots & a_{1,n} \\
       \vdots & \ddots & \vdots \\
       a_{m,1} & \cdots & a_{m,n}
    \end{pmatrix} +
    \begin{pmatrix}
       b_{1,1} & \cdots & b_{1,n} \\
       \vdots & \ddots & \vdots \\
       b_{m,1} & \cdots & b_{m,n}
    \end{pmatrix} =
    \begin{pmatrix}
       a_{1,1} + b_{1,1} & \cdots & a_{1,n} + b_{1,n} \\
       \vdots & \ddots & \vdots \\
       a_{m,1} + b_{m,1} & \cdots & a_{m,n} + b_{m,n}
    \end{pmatrix}

We see that the resulting matrix is again a :math:`m \times n` matrix.
The common `rules of associativity and commutativity <https://de.wikipedia.org/wiki/Matrizenaddition#Eigenschaften>`_ also apply here.

More interesting is the multiplication of the :math:`m \times n` matrix :math:`\text{A}` with the :math:`n \times p` matrix :math:`\text{B}` which
results in a :math:`m \times p` matrix :math:`\text{C}` as

.. math::

    \text{A} \text{B} =
    \begin{pmatrix}
       a_{1,1} & \cdots & a_{1,n} \\
       \vdots & \ddots & \vdots \\
       a_{m,1} & \cdots & a_{m,n}
    \end{pmatrix}
    \begin{pmatrix}
       b_{1,1} & \cdots & b_{1,p} \\
       \vdots & \ddots & \vdots \\
       b_{n,1} & \cdots & b_{n,p}
    \end{pmatrix} =
    \begin{pmatrix}
       c_{1,1} & \cdots & c_{1,p} \\
       \vdots & \ddots & \vdots \\
       c_{m,1} & \cdots & c_{m,p}
    \end{pmatrix}
    = \text{C}

where :math:`c_{i,j} = \sum_{k=1}^{n} a_{i,k} b_{k, j}`.

The multiplication of matrices is not commutative as :math:`\text{A} \text{B}` returns a :math:`m \times p` matrix but
:math:`\text{B} \text{A}` is not defined if :math:`m \neq p`.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/e/eb/Matrix_multiplication_diagram_2.svg
    :alt: Matrix multiplication

    A visual representation of matrix multiplication.
    `Source <https://en.wikipedia.org/wiki/File:Matrix_multiplication_diagram_2.svg>`__

Now lets take a look at the multiplication of a :math:`m \times n` matrix :math:`\text{A}` with a :math:`n \times 1` column vector :math:`\text{b}`.
We say *column vector* because for this operation we will simply add a single dimension to :math:`\text{b}` so it becomes basically a matrix.

.. math::

    \text{A} \text{b} &= 
    \begin{pmatrix}
       a_{1,1} & \cdots & a_{1,n} \\
       \vdots & \ddots & \vdots \\
       a_{m,1} & \cdots & a_{m,n}
    \end{pmatrix}
    \begin{pmatrix}
       b_{1} \\
       \vdots \\
       b_{n} 
    \end{pmatrix}
    =
    \begin{pmatrix}
       a_{1,1}b_1  + \cdots + a_{1,n}b_n \\
       \vdots \\
       a_{m,1}b_1 + \cdots + a_{m,n}b_n
    \end{pmatrix}

The result is a :math:`m \times 1` column vector.

When we want to multiply a vector :math:`\text{v}` to the left side of a matrix we need to *transpose* the vector (written as :math:`\text{v}^\top` to match the
dimensions of the matrix.

.. math::

    \text{v} =
    \begin{pmatrix}
       v_{1} \\
       \vdots \\
       v_{n} 
    \end{pmatrix} \Rightarrow
    \text{v}^\top =
    \begin{pmatrix}
       v_{1} & \cdots & v_{n} 
    \end{pmatrix}

:math:`\text{v}^\top` is also called a :math:`1 \times n` row vector.

Now our example from above but this time we use a :math:`m`-dimensional vector :math:`d` instead to match the dimensions:

.. math::

    \text{d}^\top \text{A} &= 
    \begin{pmatrix}
       d_{1} & \cdots & d_{m} 
    \end{pmatrix}
    \begin{pmatrix}
       a_{1,1} & \cdots & a_{1,n} \\
       \vdots & \ddots & \vdots \\
       a_{m,1} & \cdots & a_{m,n}
    \end{pmatrix} \\ &=
    \begin{pmatrix}
       a_{1,1}d_1 + a_{2,1}d_2 + \cdots + a_{1,m}d_m  & \cdots & a_{1,n}d_1 + a_{2,n}d_2 + \cdots + a_{n,m}d_m
    \end{pmatrix}

The result is now a :math:`n` dimensional row vector.

Statistics
----------

`Machine learning is not just statistics on big-data <https://towardsdatascience.com/the-actual-difference-between-statistics-and-machine-learning-64b49f07ea3>`__
but machine learning relies heavily on statistics to work properly.
Statistics helps us to navigate, interpret and understand a dataset and is therefore a mighty tool as it tries to make simplifications on complex structures.

A *random variable* :math:`X: \Omega \rightarrow E` is a function which accounts the possibility of outcomes in the *space of all possible outcomes* :math:`\Omega`
to a *measurable space* :math:`E`.
What a *measurable space* is exactly is `a lecture on its own <https://en.wikipedia.org/wiki/Measure_(mathematics)>`__.
The *realization* :math:`x` of :math:`X(\omega) = x` for :math:`\omega \in \Omega` can be regarded as an *outcome* of an *experiment*.

Taking a coin toss as an example: The possible outcomes are *heads* (0) or *tails* (1), so :math:`\Omega_{\text{coin}} = \lbrace 0, 1 \rbrace`.

.. todo::

    We define the *probability* that :math:`X` has an *outcome* :math:`S \subset E` by

    .. math::

        \mathbb{P} (X \in S) = \mathbb{P}(\lbrace \omega \in \Omega | X(\omega) \in S \rbrace )

    where :math:`\mathbb{P}` is a

We can also write down the *possibilities* of the random variable :math:`X` in this example:

.. math::

    \mathbb{P}_X(x) = 
    \begin{cases}
        \frac{1}{2}, &x \in \{0,\}\\
        \frac{1}{2}, &x \in \{1\}
    \end{cases}

We call this the *probability mass function*.

But this seems pretty obvious but what do we do if we do not have a discrete, finite set of outcomes but an
infinite, continuous set of outcomes?
We do not want to write down infinite outcomes and even then: To probability to observe a single outcome :math:`c` in
an infinite space of outcomes is :math:`0`.
But what we can do is describe the likelihood of to observe this particular sample relative to all observable samples.
A *probability density function* (pdf) is exactly this and gives us a way to calculate the 
probabilities of a continuous random variables.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/8/8c/Standard_deviation_diagram.svg
    :alt: plot of the standard normal distribution

    A common probability density function is the *standard normal distribution*.
    `Source <https://en.wikipedia.org/wiki/Normal_distribution#/media/File:Standard_deviation_diagram.svg>`__

The *expectation* :math:`\mathbb{E}[X]` of a discrete random variable :math:`X` with :math:`\Omega = \{ x_i \}_{i=1}^{m}` is given by

.. math::

    \mu_{X} = \mathbb{E}[X] := \sum_{i=1}^{m} x_i \mathbb{P}(X = x_i)

Once again an example: Consider a dice - its possible outcomes are all numbers between 1 and 6, so
:math:`\Omega_{\text{dice}} = \{ 1, 2, 3, 4, 5, 6 \}`.
To dice any of the numbers is equally likely so :math:`\mathbb{P}_X(x) = \frac{1}{|\Omega_{\text{dice}}|} = \frac{1}{6}`.
Putting everything together we can now calculate the expectation :math:`\mathbb{E}[X_{\text{dice}}]`:

.. math::

    \mu_{X_{\text{dice}}} = \mathbb{E}[X_{\text{dice}}] = \sum_{i=1}^{6} i \frac{1}{6} = 1\frac{1}{6} + 2 \frac{1}{6} + \cdots + 6\frac{1}{6} = 3.5

It is important to understand that :math:`\mu_{X_{\text{dice}}} \notin \Omega_{\text{dice}}` - the *expectation* itself must not be possible - it is
more like the average value that can be expected.

But most of the time we not only take a look at the expected value of a random variable but also how far the realizations of the
random variable are away from the expected value.
For example we create a new dice :math:`\alpha` - but this time the surface only has two numbers on all 6 sides,
so :math:`\Omega_{\text{dice}_{\alpha}} = \{ 2,5 \}`.
We can also calculate the expectation for our new dice:

.. math::

    \mu_{X_{\text{dice}_\alpha}} = \mathbb{E}[X_{\text{dice}_\alpha}] = \sum_{i \in \Omega_{\text{dice}_{\alpha}}} i \frac{1}{|\Omega_{\text{dice}_{\alpha}}|} = 2\frac{1}{2} + 5 \frac{1}{2} = 3.5

We can use the *variance* :math:`\sigma^2` to still distinguish the random variables from our normal dice and dice :math:`\alpha`.

.. math::

    \sigma_X^2 = \text{var}_X = \mathbb{E}[(X - \mu_X)]

For a discrete random variable :math:`X` we can use

.. math::

    \sigma_X = \sqrt{\sum_{\omega \in \Omega} \mathbb{P}(X=\omega) (\omega - \mu_X)^2}

.. todo::

    * Quantiles
    * Distributions
    * Accuracy vs precision
