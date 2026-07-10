# Examples

<div style="text-align: center; padding: 1rem 0 1.5rem;">
  <p style="font-size: 1.1rem; color: var(--md-default-fg-color--light); max-width: 640px; margin: 0 auto;">Three real runs of the schematize pipeline, end to end: the clarification chat, then the extraction schema it produced.</p>
</div>

Each case below is a real, unedited pipeline run against a real research question — no cherry-picking of a "nice" answer. All runs were conducted in Polish; the assistant's longer turns are condensed for readability. The same case was then run through five different LLMs, so you can compare how schema shape and coverage change with the model.

!!! warning "About the English text on these pages"
    Every run shown here was performed in Polish — the prompts, conversation, and generated schema
    field descriptions are all originally in Polish. The English versions on each page are **machine
    translations** produced after the fact for readability, not translations reviewed by a native
    speaker. If anything reads oddly in English, treat the Polish tab as the source of truth.

<div class="grid cards case-cards" markdown>

-   **[:material-gavel: Age at Sentencing](age.md)**

    ---

    Does a defendant's age predict the type and severity of the sentence in drug-offense cases?

-   **[:material-hospital-box: Medical Malpractice Compensation](medical_errors.md)**

    ---

    What drives the amount of compensation Polish civil courts award for medical errors?

-   **[:material-account-alert: Personal Rights Violations](personal_rights.md)**

    ---

    Are personal-rights lawsuits becoming more trivial over time?

</div>

Want to try it on your own question? See the [quickstart](../quickstart.md) or [pipeline overview](../pipeline.md).
