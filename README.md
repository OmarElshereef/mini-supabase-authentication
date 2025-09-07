# mini-supabase-authentication

A minimal FastAPI implementation demonstrating custom token management with Supabase authentication, bypassing the automatic token refresh mechanism for manual control.

## Overview

This project showcases how to implement custom token refresh logic in a FastAPI application using Supabase authentication. By disabling the automatic token refresh feature, developers gain full control over when and how authentication tokens are refreshed, enabling custom authentication flows and better integration with existing systems.

## Features

- Manual Token Management: Disable automatic token refresh for precise contro

- Custom Refresh Endpoint: Implement your own token refresh logic

## Requirements

- Python 3.13 or later

#### Instal Python using MiniConda

1. Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install)
2. create a new environment using the following command:

```bash
$ conda create -n supabase-auth
```

3. activate the environmentL

```bash
$ conda activate supabase-auth
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your env variables in the .env file like "SUPABASE_URL" value.

## Run the FastAPI server

```bash
$ uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```
