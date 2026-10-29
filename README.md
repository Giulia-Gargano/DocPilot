# DocPilot

An evidence-first document assistant built with Python.

DocPilot aims to answer questions about technical documentation
using retrieval-augmented generation (RAG), with traceable sources
and measurable quality.

## Project status

Early development. No working demo or benchmark results yet.

## The problem

Finding accurate answers across technical documentation takes time.
AI-generated answers also need supporting evidence that users can verify.

## Planned solution

DocPilot will retrieve relevant document passages and use them
to generate answers with source references.

When the documents do not contain enough information, the assistant
should clearly state that it cannot answer from the available evidence.

## Initial scope

The first version will use a small, curated collection of public
technical documentation.

The initial goal is a reproducible question-answering pipeline,
not a general-purpose autonomous agent.

## Roadmap

- [x] Create the GitHub repository
- [ ] Select the document collection and record its sources
- [ ] Implement text extraction and chunking
- [ ] Build a baseline retrieval pipeline
- [ ] Generate answers with source references
- [ ] Create a manually reviewed evaluation dataset
- [ ] Measure retrieval and answer quality
- [ ] Expose the pipeline through a FastAPI endpoint
- [ ] Add automated tests and continuous integration
- [ ] Publish a demo and reproducible benchmark results

## Planned evaluation

- Retrieval recall at k
- Answer faithfulness
- Correct abstention on unanswerable questions
- End-to-end latency
- Estimated model cost per query

Results will be published only after running the evaluation.

## Engineering principles

- Start with a simple, measurable baseline.
- Keep source metadata throughout the pipeline.
- Separate retrieval quality from generation quality.
- Keep API keys and private documents out of version control.
- Document limitations and failed experiments.

## Author

Giulia Gargano
