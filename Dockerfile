ARG PYTHON_BASE=3.12.4-slim

#build stage
FROM python:$PYTHON_BASE AS builder

RUN pip install -U pdm

ENV PDM_CHECK_UPDATE=false

COPY pyproject.toml pdm.lock README.md /project/
COPY app/ /project/app

WORKDIR /project
RUN pdm install --check --prod --no-editable

#run stage
FROM python:$PYTHON_BASE as executor

COPY --from=builder /project/.venv/ /project/.venv
ENV PATH="/project/.venv/bin:$PATH"
COPY app/ /project/app

CMD ["python3", "/project/app/__init__.py"]