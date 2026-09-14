# Global Population & Geopolitical Risk Dashboard

AI Applications practical project for the Department of FinTech / AI Applications.

## Project Overview

This project explores two major global issues:

1. Long-term global population change.
2. Geopolitical risks related to Iran and the Middle East.

The project combines Python data processing, JSON, responsive web development and AI-assisted research.

## Research Claim

Global population is expected to continue growing during much of the 21st century, while geopolitical instability in the Middle East may simultaneously affect global energy markets, supply chains, inflation and policy planning.

## Population Data

Primary source:

United Nations, World Population Prospects 2024.

Cross-check source:

Our World in Data, using UN World Population Prospects 2024 data.

Selected population values:

* 2024: 8.162 billion
* 2030: 8.569 billion
* 2050: 9.664 billion
* 2100: 10.180 billion

The figures use the UN medium projection scenario.

## Python Data Processing

The raw population data is stored in:

`data/raw.txt`

The Python processing script is stored in:

`scripts/clean.py`

The Python script:

* reads the raw data;
* removes comments and unnecessary text;
* converts population values into structured data;
* calculates the selected-year average;
* calculates total population growth;
* calculates CAGR;
* calculates growth between selected periods;
* exports the results as JSON.

The resulting data is stored in:

`data/cleaned.json`

The website reads this JSON file using JavaScript.

## Calculated Results

Selected-year average population:

9.14375 billion.

Growth from 2024 to 2100:

approximately 24.72%.

CAGR from 2024 to 2100:

approximately 0.291% per year.

## Iran Risk Matrix

The dashboard evaluates four major risk factors:

* nuclear and safeguards risk;
* Strait of Hormuz and energy shipping disruption;
* international sanctions and economic pressure;
* regional armed groups and escalation.

Risk ratings such as Low, Medium and High are analytical judgments made for this project. They are not probability ratings directly published by the source organizations.

Sources include:

* International Atomic Energy Agency (IAEA);
* U.S. Energy Information Administration (EIA);
* Reuters.

## Fact vs. Inference

The project separates factual evidence from analytical inference.

Facts are statements that can be directly supported by external sources.

Inference refers to conclusions derived from those facts, such as assigning a High, Medium or Low risk level.

This separation is important because geopolitical analysis contains uncertainty.

## AI Usage Statement

Generative AI was used as an assistant during this project.

AI was used to help:

* organize the project structure;
* generate and review Python code;
* develop HTML, CSS and JavaScript;
* improve responsive web design;
* identify possible geopolitical risk categories;
* summarize source material;
* review wording and documentation.

AI-generated information was not automatically treated as factual.

Important numerical and geopolitical claims were checked against external sources.

## Example Prompts

Example Prompt 1:

“Using UN World Population Prospects 2024, help me organize population values for 2024, 2030, 2050 and 2100 and explain how to calculate growth rate and CAGR.”

Example Prompt 2:

“Write a Python program that reads population data from a raw text file, calculates average population, growth rate and CAGR, and exports the result to JSON.”

Example Prompt 3:

“Create a responsive HTML dashboard displaying population data from JSON. The design must work on mobile devices.”

Example Prompt 4:

“Identify four major geopolitical risks related to Iran. Clearly separate verified facts from analytical inference and do not invent unsupported information.”

## Validation Process

The following validation process was used:

1. Ask AI for an initial answer.
2. Identify numerical or factual claims.
3. Locate the original or authoritative source.
4. Compare the AI answer with UN, IAEA or EIA data.
5. Use Reuters for recent event verification when appropriate.
6. Correct any inconsistent numbers.
7. Clearly mark analytical conclusions as inference.

## Differences Between AI Answers

Different AI systems may return different population projections because they may use different editions of the UN World Population Prospects.

For example, an AI model may use an older population projection and return a different population for 2100.

To resolve this problem, this project uses a single consistent dataset: UN World Population Prospects 2024.

The publication year and projection scenario are always checked before accepting an AI-generated number.

## Avoiding AI Hallucination

To reduce hallucination risk:

* numerical claims require identifiable sources;
* authoritative primary sources are preferred;
* important claims are cross-checked;
* facts and interpretations are separated;
* geopolitical probability ratings are labeled as analytical judgments;
* uncertain information is not presented as confirmed fact.

## Responsive Design

The website uses CSS media queries and responsive layouts to support desktop and mobile screens.

Large external libraries and images were avoided to improve mobile performance.

## Repository Structure

```text
.
├── index.html
├── style.css
├── app.js
├── README.md
├── data
│   ├── raw.txt
│   └── cleaned.json
└── scripts
    └── clean.py
```

## Technologies

* HTML5
* CSS3
* JavaScript
* Python
* JSON
* Git
* GitHub
* GitHub Pages
* Generative AI

## Author

王韡儒

Department of FinTech / AI Applications
