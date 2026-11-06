# AI-assisted OSINT

AI can help structure research, summarize documents and identify questions for further checking. It can also hallucinate sources, dates, quotes and causal links. Never treat an AI answer as evidence.

## Research prompt

```text
Act as a research assistant working only with lawfully accessible public sources.
Question: [INSERT QUESTION]
Time window: [INSERT WINDOW]
Geographic scope: [INSERT SCOPE]

Find primary sources first, then independent corroboration.
For each claim, provide:
- exact claim
- source title and publisher
- publication date and event date (if different)
- direct URL
- what the source actually establishes
- limitations or possible bias

Label each item as CONFIRMED FACT, ATTRIBUTED STATEMENT,
ASSESSMENT, HYPOTHESIS or UNVERIFIED.

Do not invent citations, quotations, dates or sources.
If you cannot open or verify a source, say so.
Distinguish independent sources from outlets repeating the same report.
Consider alternative explanations and missing evidence.
Do not identify private individuals, expose personal data,
or provide real-time tactical tracking or targeting assistance.

Finish with:
1. What is established
2. What remains uncertain
3. What evidence would resolve the uncertainty
4. A concise source list
```

## Human verification checklist

- Open every cited URL.
- Confirm that the page supports the exact sentence.
- Check publication and event dates.
- Verify quotations against the original.
- Check whether sources are independent.
- Remove unsupported claims and fabricated references.
- Record the AI tool and date used when relevant.
