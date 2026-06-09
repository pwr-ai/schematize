# Expert Evaluation File Generation Guide

## Overview

This document summarizes the process and best practices for generating expert evaluation files based on case dialogs in the schema generation system.

## Purpose

Expert evaluation files contain questions that extraction schemas should answer. These questions are used to evaluate whether the generated schema captures all necessary information for a researcher's study.

## Process

### 1. Analyze the Case Dialog

Each case file contains a three-part dialog:
- `user_input`: Initial request from researcher
- `problem_help`: AI bot's clarifying questions and suggestions
- `user_feedback`: Researcher's responses and refinements

**Key task:** Understand what the researcher actually wants to study based on:
- What they confirmed (yes/no answers)
- What they explicitly rejected
- Additional comments with specific requirements

### 2. Create Expert Profiles

Generate 3+ independent experts, each with:

**Profile components:**
- Name and professional title
- Area of specialization
- Research focus (2-3 paragraphs)
- Methodological approach and personality

**Key principles:**
- Each expert should have a distinct disciplinary perspective (e.g., criminologist, legal scholar, sociologist)
- Experts should have overlapping but not identical interests 
- Different question counts are fine
- Experts must respect boundaries set in the dialog

### 3. Define Research Focus

For each expert, elaborate on what they would study:
- Core research question
- Why they care about this particular aspect
- What they hope to discover or prove
- Their analytical approach

**Remember:** You can be creative and elaborate beyond what's in the dialog, as long as it doesn't contradict the user's stated preferences.

### 4. Generate Evaluation Questions

Questions should:
- Cover all aspects mentioned in user feedback
- Include factors that could influence the studied phenomenon
- Capture both direct and indirect influences
- Be specific and answerable from court judgments
- Use clear, unambiguous language

**Question categories to consider:**
- Demographics and basic case facts
- Primary outcomes (sentences, fines, etc.)
- Contextual factors (prior convictions, circumstances)
- Aggravating/mitigating factors
- Personal circumstances (employment, family, health)
- Procedural aspects (plea, legal representation)
- Court reasoning and justification
- Treatment/rehabilitation requirements
- Temporal information (dates, durations)

### 5. Validate Alignment

Check each expert profile against the case dialog:

**Must include:**
- All core requirements from user_input
- All confirmed suggestions from problem_help
- All specific details from user_feedback

**Must NOT include:**
- Topics explicitly rejected by user
- Jurisdictional/temporal comparisons if user said "no"
- Scope beyond what was discussed (unless it's a natural elaboration)

**Alignment scoring:**
- 85%+: Excellent alignment
- 70-84%: Good alignment, minor deviations
- 60-69%: Acceptable but needs refinement
- <60%: Poor alignment, significant contradictions

## Example: Age/Drug Possession Case

### User Requirements
- Drug possession only (not trafficking)
- Focus on defendant's age and fine amount
- Include sentence types (imprisonment, probation, community service)
- Include prior convictions and aggravating/mitigating factors
- Age categorized into 5 groups
- Drugs defined by Controlled Substances Act
- NOT interested in temporal trends or jurisdictional comparisons

### Expert Profiles Created

**Expert 1 - Criminologist (38 questions)**
- Focus: How age influences sentencing disparities
- Approach: Comprehensive data collection of individual cases
- Emphasis: Interaction between age and other case characteristics

**Expert 2 - Legal Scholar (35 questions)**
- Focus: Proportionality principle in sentencing
- Approach: Doctrinal-empirical analysis
- Emphasis: Court reasoning and legal justification

**Expert 3 - Sociologist (33 questions)**
- Focus: Social inequality in sentencing outcomes
- Approach: Critical perspective on formal vs. substantive equality
- Emphasis: Social circumstances and reintegration potential

### Key Fixes Applied

**Expert 1:** Removed "victim impact" (not relevant for simple possession), consolidated date questions

**Expert 3:** Removed "geographic location or jurisdiction" (contradicted user's stated disinterest in jurisdictional comparisons), added clarification about focusing on individual cases

## Common Pitfalls

1. **Over-generalizing expert approach:** Avoid making experts sound like they'd push back or ask more clarifying questions than the user wanted

2. **Ignoring explicit rejections:** If user says "no, I'm not interested in that," experts should not ask related questions

3. **Forcing too much differentiation:** Experts naturally share core interests; 70-80% overlap is realistic and appropriate

4. **Losing specificity:** Questions should reference specific legal concepts (e.g., "Controlled Substances Act") when mentioned in dialog

5. **Missing indirect factors:** Complex legal research requires questions about tangential factors that could influence outcomes

## Tips for Quality

- **Personality matters:** Give each expert a distinct voice and methodological style
- **Context is key:** Questions should be answerable from court documents
- **Think like a researcher:** What would this person want to prove or disprove?
- **Balance breadth and focus:** Comprehensive but within agreed scope
- **Natural variation:** Question counts can vary; quality over uniformity

## File Format

```yaml
# Expert: [Full name], [Title and specialization]
#
# Research focus: [2-3 paragraphs describing what they study,
# why it matters, their approach, and personality]

questions:
  - [Question 1]
  - [Question 2]
  - [Question N]
```

## Future Applications

This process can be applied to any case type:
- Contract disputes
- Personal rights violations
- Property law
- Employment law
- Family law
- Administrative decisions

The key is always to start with the case dialog and ensure experts respect the researcher's stated scope while bringing their unique disciplinary perspectives.



