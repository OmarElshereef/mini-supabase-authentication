# mini-supabase-authentication

this is a minimal implementaion of supabase authentication service.

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
