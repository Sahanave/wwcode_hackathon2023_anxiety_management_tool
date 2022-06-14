# Prototyping a Machine Learning Application with Streamlit

[Streamlit](https://streamlit.io) is a free, open-source, all-python framework
that enables data scientists to quickly build interactive dashboards and machine
learning web apps with no front-end web development experience required.

- [Prototyping a Machine Learning Application with Streamlit](#prototyping-a-machine-learning-application-with-streamlit)
  - [What is Prototyping?](#what-is-prototyping)
    - [Prototyping Tools](#prototyping-tools)
  - [What is Streamlit?](#what-is-streamlit)
    - [Why use Streamlit](#why-use-streamlit)
  - [Example](#example)
    - [Architecture](#architecture)
    - [Project Setup](#project-setup)
      - [Clone this repository](#clone-this-repository)
      - [Configure environment](#configure-environment)
    - [Tools](#tools)

## What is Prototyping?

[Prototyping](https://www.interaction-design.org/literature/topics/prototyping) is a process to develop an idea and it is used in different areas to test or simulate that idea before launching it.

* [Prototype](https://en.wikipedia.org/wiki/Prototype) is a version of what the product would be.
* Prototyping is the iterative process of idea development.

> "in the **prototyping** process we will have some **prototypes** of an idea"

Prototyping is a fundamental step for any type of product, idea or service because it allows:

* develop an initial version of the idea,
* discover flaws,
* reduce costs,
* know the users experience,
* test features,
* and also generate [POCs](https://en.wikipedia.org/wiki/Proof-of-concept) or [MVPs](https://en.wikipedia.org/wiki/Minimum_viable_product) of the idea.

### Prototyping Tools

There are different tools according to the level of fidelity or similarity between the idea and the final product. These levels can vary in the conceptual, aesthetic and functional.

* Low-fidelity prototyping is a paper draft of the idea.
* Mid-fidelity prototyping can be produced in software a mockup, replicating some fundamental functionalities of the idea. Some tools such as [Figma](https://www.figma.com), [Sketch](https://www.sketch.com), [Miro](https://miro.com), [InVision](https://www.invisionapp.com).
* High-fidelity prototype may include some level of programming to fluidly replicate the behavior of the final solution. Some tools such as [Flask](https://flask.palletsprojects.com/en/2.1.x/), [Streamlit](https://streamlit.io).

## What is Streamlit?

### Why use Streamlit

I think it could be a good option when you want to get a
[prototype](https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila)
of your dashboard/web app up and running as quickly as possible.

## Example

### Architecture

![streamlit basic architecture](assets/streamlit-basic.png)

### Project Setup

Installing Streamlit is as simple as installing any other Python package.

#### Clone this repository

```shell
(base)$: git clone git@github.com:mafda/data_science_with_fastapi_and_streamlit.git
(base)$: cd data_science_with_fastapi_and_streamlit
```

#### Configure environment

- Create the conda environment

```shell
(base)$: conda env create -f environment.yml
```

- and update with **development dependencies** (Read more about [Python Best
  Practices](https://github.com/mafda/python_best_practices))

```shell
(base)$: conda env update -n ds-app -f environment-dev.yml
```

- Activate the environment

```shell
(base)$: conda activate ds-app
(base)$: git checkout streamlit-basic
```

- Run

```shell
(ds-app)$: streamlit run src/app.py
```

- And go to [http://localhost:8501](http://localhost:8501)

### Tools

- [Streamlit](https://streamlit.io)


---

made with 💙 by [mafda](https://mafda.github.io/)
