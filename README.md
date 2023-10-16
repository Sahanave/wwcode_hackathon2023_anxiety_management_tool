# Anxiety Management Platform using AI

This repository is built upon the foundations provided by [mafda's work on ML with FastAPI and Streamlit](https://github.com/mafda/ml_with_fastapi_and_streamlit). Our project focuses on developing a personalized AI-driven platform for anxiety management.

## Table of Contents

- [Overview of the Project](#overview-of-the-project)
- [Why Streamlit?](#why-use-streamlit)
- [FastAPI in Action](#what-is-fastapi)
- [The Power of Hugging Face](#what-is-hugging-face)
- [System Architecture](#architecture)
- [Setting Up the Project](#project-setup)
- [Outcome & Screenshots](#results)
- [Final Thoughts](#conclusions)
- [Tools Used](#tools)

## Overview of the Project

The main goal of this platform is to provide a tailored approach to anxiety management by leveraging the power of AI. Using Streamlit for interface design, FastAPI for backend services, and Hugging Face for NLP functionalities, we aim to provide therapists and patients a tool that is both engaging and effective.

## Why Streamlit?

[Streamlit](https://streamlit.io) is a user-friendly Python framework, allowing for the creation of interactive dashboards and web apps without requiring extensive web development experience. Given its compatibility with various ML and visualization libraries, it's an ideal choice for this project.

## FastAPI in Action

[FastAPI](https://fastapi.tiangolo.com) offers a fast and efficient means to build APIs using Python. 

## The Power of Hugging Face

[Hugging Face](https://huggingface.co) brings the might of NLP to our platform. With its vast resources and libraries, we can provide users with intelligent and personalized content to aid their therapeutic journey.

### Architecture

![System Architecture](assets/streamlit-fastapi.png)

### Setting Up the Project

- Start by cloning this repository:

```shell
(base)$: git clone [your-repo-link]
(base)$: cd [your-repo-directory]
```

- Launch the platform:

```shell
$ docker-compose up
```

- Access the interface at [http://localhost:8501](http://localhost:8501)

## Outcome & Screenshots

![Sample Outcome](assets/sample-outcome.gif)

## Final Thoughts

Combining Streamlit, FastAPI, and Hugging Face provides a swift and efficient way to prototype, create MVPs, and launch applications in a minimal timeframe. This blend proves invaluable for projects aiming for rapid deployment and immediate user feedback.
