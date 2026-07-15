# Medical Malpractice Compensation

How civil courts determine compensation and damages for medical malpractice.

!!! info "About the English text on this page"
    This run was performed in Polish — the prompts, conversation, and generated schema field
    descriptions are all originally in Polish. The English tabs are machine translations
    produced after the fact for readability.

## The conversation

=== "🇬🇧 English"

    <div class="chat" markdown="1">
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">You</span>

    How do civil courts determine the amount of compensation for pain and suffering (zadośćuczynienie) in medical malpractice cases, and what circumstances affect the amounts awarded to patients?

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Assistant</span>

    1. [Confirmation] I understand you want to study which criteria and arguments civil courts cite when setting the amount of compensation for harm caused by medical malpractice, and which circumstances correlate with the amounts awarded — is that right?

    2. [Confirmation] Are you interested only in monetary compensation for non-pecuniary harm ("zadośćuczynienie", Art. 445 §1 / 448 Civil Code), or also related claims such as damages for pecuniary loss ("odszkodowanie", Art. 444) and an annuity ("renta", Art. 444 §2)?

    3. [Legal framework] Is it important to distinguish the basis of liability — tort liability, vicarious/risk-based liability for a subordinate, and the liability of the medical entity (e.g. organizational fault) — and do you want to check whether the choice of legal basis affects the amount awarded?

    4. [Procedural context] Do you want to compare how first- and second-instance courts assess the amount (including how often the appellate court changes it), as one of the main study variables?

    5. [Procedural context] Are you interested in whether the defendant's status (a physician as an individual, a hospital/medical entity, or a liability insurer) differentiates the amount awarded or how it's justified?

    6. [Case-law analysis] Do you want to study the influence of expert opinions (e.g. findings on causation, degree of permanent health impairment, prognosis) on the amount awarded, and which elements of the opinion courts treat as decisive?

    7. [Case-law analysis] Which substantive circumstances should be the key potential "amount determinants" for you — e.g. duration and intensity of suffering, irreversibility of effects, patient's age, disability, loss of independence, impact on family and professional life?

    8. [Case-law analysis] Are you interested in how courts justify the "appropriateness" of the amount — e.g. whether they compare it to other rulings, invoke a compensatory function, or reference the standard of living — and do you want to compare these argumentation patterns across courts?

    9. [Temporal context] Do you want to study whether the practice of awarding amounts has changed over time (e.g. an upward trend), and whether courts link this to factors such as inflation or evolving patient-protection standards?

    10. [Special cases] Do you want to separate out specific categories of errors and consequences (e.g. diagnostic vs. treatment vs. perinatal error; patient death and claims by relatives) and compare whether these case types lead to significantly different amounts and different reasoning?

    </div>
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">You</span>

    1. Yes, I want to find the variables that predict the amount.
    2. Compensation (zadośćuczynienie) and damages (odszkodowanie). Not the annuity.
    3. No, the legal basis isn't a variable I care about.
    4. Yes, I want to know how often the appellate court changes the amount, and in which direction.
    5. Yes, especially the difference between a hospital and an insurer.
    6. Yes. Whether the court based the amount on the percentage impairment from the expert opinion, or went beyond it.
    7. All the circumstances listed matter.
    8. Yes, whether courts compare themselves to other rulings, and whether they do so explicitly.
    9. No.
    10. Yes, categorize the errors and consequences.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Assistant</span>

    We're studying how civil courts determine the amount of compensation (zadośćuczynienie) and damages (odszkodowanie) for medical malpractice, and which circumstances predict the amount awarded. We account for the defendant's type (hospital, physician, insurer), the role of expert opinions (including percentage health impairment), differences between first and second instance, and the category of medical error and its consequences for the patient (pain and suffering, permanent impairment, disability, impact on family and professional life, death). The legal basis is Art. 445 and 448 KC (compensation) and Art. 444 KC (damages); the choice of liability basis is not a separate study variable.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Assistant</span>

    Based on your question, I've prepared an extraction schema for analyzing civil rulings in medical malpractice cases, to check which circumstances predict the amount of compensation and damages awarded and how courts justify those amounts. The schema targets patient cases against hospitals, medical entities, physicians, and insurers, covering both first instance and whether the appellate court changes the amount, and in which direction.

    The generated schema includes fields to capture the claim type and outcome, amounts claimed and awarded, the distinction between compensation and damages, the defendant type, the type of medical error, and consequences for the patient such as pain and suffering, permanent impairment, disability, loss of independence, impact on family and professional life, or death. It also extracts information about the expert opinion, including the percentage health impairment and whether the court based the amount on it, as well as whether the court explicitly compared the case to other rulings and invoked the compensatory function and an individualized assessment of harm.

    The schema also lets you separately record the different categories of medical error, the consequence for the patient, and how the awards were assessed, so you can later study which variables actually correlate with the amounts awarded. If you'd like, you can now point out anything to refine, simplify, or add.

    </div>
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">You</span>

    I'm satisfied. I want to end the chat.

    </div>
    </div>

    *The clarifying questions and answers are shown verbatim; the assistant's longer turns are condensed for readability. The English text is machine-translated from the original Polish run.*

=== "🇵🇱 Polski"

    <div class="chat" markdown="1">
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">Ty</span>

    W jaki sposób sądy cywilne ustalają wysokość zadośćuczynienia za błędy medyczne i jakie okoliczności wpływają na kwoty zasądzane na rzecz pacjentów?

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Asystent</span>

    1. [Potwierdzenie] Rozumiem, że chcesz zbadać, jakie kryteria i argumenty sądy cywilne wskazują w uzasadnieniach wyroków przy ustalaniu wysokości zadośćuczynienia za krzywdę wynikłą z błędu medycznego oraz które okoliczności korelują z wysokością zasądzanych kwot — czy dobrze rozumiem?

    2. [Potwierdzenie] Czy interesuje Cię wyłącznie zadośćuczynienie pieniężne za doznaną krzywdę (art. 445 § 1 Kodeksu cywilnego i/lub art. 448 Kodeksu cywilnego), czy także powiązane roszczenia, np. odszkodowanie (art. 444 Kodeksu cywilnego) oraz renta (art. 444 § 2 Kodeksu cywilnego)?

    3. [Ramy prawne] Czy kluczowe jest dla Ciebie rozróżnienie podstawy odpowiedzialności: odpowiedzialność deliktowa (art. 415 k.c.), odpowiedzialność na zasadzie ryzyka za podwładnego (art. 430 k.c.) oraz odpowiedzialność podmiotu leczniczego (np. wątek winy organizacyjnej), i czy chcesz sprawdzić, czy wybór podstawy prawnej wpływa na wysokość zadośćuczynienia?

    4. [Kontekst procesowy] Czy chcesz porównywać podejście do miarkowania zadośćuczynienia między sądem pierwszej instancji a sądem drugiej instancji (w tym, jak często sądy zmieniają kwotę zasądzoną) i czy to ma być jedna z głównych zmiennych badawczych?

    5. [Kontekst procesowy] Czy interesuje Cię, czy status pozwanego (lekarz jako osoba fizyczna, szpital/podmiot leczniczy, ubezpieczyciel odpowiedzialności cywilnej) różnicuje wysokość zasądzanego zadośćuczynienia lub sposób uzasadniania?

    6. [Analiza orzecznictwa] Czy chcesz badać wpływ opinii biegłych (np. ustaleń co do związku przyczynowego, stopnia trwałego uszczerbku na zdrowiu, rokowań) na wysokość zadośćuczynienia i na to, jakie elementy opinii sądy uznają za decydujące?

    7. [Analiza orzecznictwa] Które okoliczności materialnoprawne mają być dla Ciebie kluczowe jako potencjalne „determinanty kwoty” — np. czas trwania i intensywność cierpień, nieodwracalność skutków, wiek pacjenta, niepełnosprawność, utrata samodzielności, wpływ na życie rodzinne i zawodowe?

    8. [Analiza orzecznictwa] Czy interesuje Cię, w jaki sposób sądy uzasadniają „odpowiedniość” zadośćuczynienia — np. czy odwołują się do porównania z innymi orzeczeniami, do funkcji kompensacyjnej, do stopy życiowej społeczeństwa, i czy te wzorce argumentacyjne chcesz porównać między sądami?

    9. [Kontekst temporalny] Czy chcesz zbadać, czy w czasie zmieniała się praktyka zasądzania kwot (np. trend wzrostowy) oraz czy sądy wiążą to z czynnikami takimi jak inflacja lub ewolucja standardów ochrony pacjenta, niezależnie od konkretnych nowelizacji?

    10. [Przypadki szczególne] Czy chcesz wyodrębnić szczególne kategorie błędów i skutków (np. błąd diagnostyczny vs błąd terapeutyczny vs błąd okołoporodowy; śmierć pacjenta i roszczenia osób bliskich na podstawie art. 446 § 4 k.c.) i porównać, czy te typy spraw prowadzą do istotnie różnych kwot i innego sposobu uzasadniania?


    </div>
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">Ty</span>

    1. Tak, chcę znaleźć zmienne, które przewidują wysokość kwoty.
    2. Zadośćuczynienie i odszkodowanie. Renty nie.
    3. Nie, podstawa prawna to nie jest moja zmienna.
    4. Tak, chcę wiedzieć jak często sąd odwoławczy zmienia kwotę i w którą stronę.
    5. Tak, szczególnie różnica między szpitalem a ubezpieczycielem.
    6. Tak. Czy sąd oparł kwotę na procentowym uszczerbku z opinii biegłego, czy wyszedł poza nią.
    7. Wszystkie wymienione okoliczności są ważne.
    8. Tak, czy sądy porównują się do innych wyroków i czy robią to wprost.
    9. Nie.
    10. Tak, skategoryzuj błędy i skutki. 


    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Asystent</span>

    Badamy, jak sądy cywilne ustalają wysokość zadośćuczynienia i odszkodowania za błędy medyczne oraz które okoliczności przewidują wysokość zasądzanych kwot. Uwzględniamy typ pozwanego (szpital, lekarz, ubezpieczyciel), rolę opinii biegłego (w tym procentowy uszczerbek na zdrowiu), różnice między I a II instancją oraz kategorię błędu medycznego i jego skutki dla pacjenta (ból i cierpienie, trwały uszczerbek, niepełnosprawność, wpływ na życie rodzinne i zawodowe, zgon). Podstawą prawną są art. 445 i 448 k.c. (zadośćuczynienie) oraz art. 444 k.c. (odszkodowanie); wybór podstawy odpowiedzialności nie jest osobną zmienną badawczą.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Asystent</span>

    Na podstawie Twojego pytania przygotowałem schemat ekstrakcji do analizy orzeczeń cywilnych w sprawach o błędy medyczne, żeby sprawdzać, jakie okoliczności przewidują wysokość zasądzanego zadośćuczynienia i odszkodowania oraz jak sądy uzasadniają te kwoty. Schemat jest nastawiony na sprawy pacjentów przeciwko szpitalom, podmiotom leczniczym, lekarzom i ubezpieczycielom, z uwzględnieniem zarówno I instancji, jak i tego, czy sąd odwoławczy zmienia kwotę oraz w którą stronę.

    Wygenerowany schemat obejmuje pola do uchwycenia rodzaju roszczenia i jego wyniku, kwot dochodzonych i zasądzonych, różnicy między zadośćuczynieniem a odszkodowaniem, typu pozwanego, rodzaju błędu medycznego oraz skutków dla pacjenta, takich jak ból i cierpienie, trwały uszczerbek, niepełnosprawność, utrata samodzielności, wpływ na życie rodzinne i zawodowe czy zgon. Dodatkowo wyodrębnia informacje o opinii biegłego, w tym procentowym uszczerbku na zdrowiu i tym, czy sąd oparł na nim kwotę, a także o tym, czy sąd wprost porównywał sprawę z innymi orzeczeniami i czy odwoływał się do funkcji kompensacyjnej oraz indywidualnej oceny krzywdy.

    Schemat zawiera też pola pozwalające oddzielnie opisać różne kategorie błędów medycznych, skutek dla pacjenta i sposób miarkowania świadczeń, żeby dało się później badać, które zmienne faktycznie wiążą się z wysokością zasądzanych kwot. Jeśli chcesz, możesz teraz wskazać, co mam doprecyzować, uprościć albo dodać, żeby schemat lepiej odpowiadał Twojej analizie.

    </div>
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">Ty</span>

    Jestem zadowolony. Chcę zakończyć chat.

    </div>
    </div>

    *Pytania doprecyzowujące i odpowiedzi pokazane są dosłownie; dłuższe wypowiedzi asystenta skrócono dla czytelności.*

## The generated schema

Five different LLMs ran the exact same pipeline on this case. Field count and shape vary a lot by model — pick a tab to compare.

=== "GPT-5.4"

    **150 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `case_signature` | string | Case number of the analyzed ruling, copied exactly from the header or operative part. |
        | `judgment_date_iso` | string | Normalized date the ruling was issued, in YYYY-MM-DD format. |
        | `court_name` | string | Full name of the court that issued the ruling. |
        | `court_division` | string | Name of the adjudicating division, if stated in the header. |
        | `is_document_in_scope` | enum | Whether the document falls within the scope of the study on civil medical-malpractice cases and compensation/damages amounts. |
        | `out_of_scope_reason` | enum | Main reason the document is considered out of scope or partially out of scope. |
        | `out_of_scope_secondary_reason` | enum | Additional reason for exclusion, when the document meets more than one out-of-scope category. |
        | `out_of_scope_reason_excerpt` | string | Short justification for excluding or partially excluding the document, ideally a brief quote or summary. |
        | `proceeding_type` | enum | Main type of proceeding. Use `civil_medical_malpractice` only when the case's core is civil liability for treatment, diagnosis, a procedure, childbirth, or medical care. |
        | `proceeding_type_secondary` | enum | Secondary classification of the proceeding type for borderline or mixed cases. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `case_signature` | string | Required: false. Typ: string. Sygnatura akt analizowanego orzeczenia. Przepisz dokładnie z nagłówka lub sentencji. |
        | `judgment_date_iso` | string | Required: false. Typ: string. Znormalizowana data wydania orzeczenia w formacie YYYY-MM-DD. Wypełniaj tylko gdy data wynika wprost z dokumentu. |
        | `court_name` | string | Required: false. Typ: string. Pełna nazwa sądu, który wydał analizowane orzeczenie. Przepisz z nagłówka. |
        | `court_division` | string | Required: false. Typ: string. Nazwa wydziału orzekającego, jeśli wskazana w nagłówku. |
        | `is_document_in_scope` | enum | Required: true. Typ: enum. Czy dokument mieści się w zakresie badania spraw cywilnych dotyczących błędów medycznych i analizy kwot zadośćuczynienia lub odszkodowania. To pole ma priorytet walidacyjny: gdy wartość to no, pola merytoryczne med-mal powinny pozostać puste albo przyjmować not_applicable. |
        | `out_of_scope_reason` | enum | Required: false. Typ: enum. Główny powód uznania dokumentu za poza zakresem lub częściowo poza zakresem. Dla dokumentów w pełni relewantnych użyj not_applicable. |
        | `out_of_scope_secondary_reason` | enum | Required: false. Typ: enum. Dodatkowy powód wyłączenia, gdy dokument spełnia więcej niż jedną kategorię poza zakresem. |
        | `out_of_scope_reason_excerpt` | string | Required: false. Typ: string. Krótkie uzasadnienie wyłączenia lub częściowego wyłączenia dokumentu, najlepiej w formie krótkiego cytatu albo streszczenia. |
        | `proceeding_type` | enum | Required: true. Typ: enum. Główny rodzaj postępowania. Używaj civil_medical_malpractice tylko gdy rdzeniem sprawy jest odpowiedzialność cywilna za leczenie, diagnozę, zabieg, poród lub opiekę medyczną. |
        | `proceeding_type_secondary` | enum | Required: false. Typ: enum. Pomocnicza klasyfikacja rodzaju postępowania dla przypadków granicznych lub mieszanych. |
    ??? note "Show full schema (150 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Sygnatura akt analizowanego orzeczenia. Przepisz dokładnie z nagłówka lub sentencji.",
            "name": "case_signature"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Znormalizowana data wydania orzeczenia w formacie YYYY-MM-DD. Wypełniaj tylko gdy data wynika wprost z dokumentu.",
            "name": "judgment_date_iso"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Pełna nazwa sądu, który wydał analizowane orzeczenie. Przepisz z nagłówka.",
            "name": "court_name"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Nazwa wydziału orzekającego, jeśli wskazana w nagłówku.",
            "name": "court_division"
          },
          {
            "type_": "enum",
            "enum_name": "DocumentInScope",
            "enum_values": [
              "yes",
              "no",
              "partial"
            ],
            "description": "Required: true. Typ: enum. Czy dokument mieści się w zakresie badania spraw cywilnych dotyczących błędów medycznych i analizy kwot zadośćuczynienia lub odszkodowania. To pole ma priorytet walidacyjny: gdy wartość to no, pola merytoryczne med-mal powinny pozostać puste albo przyjmować not_applicable.",
            "name": "is_document_in_scope"
          },
          {
            "type_": "enum",
            "enum_name": "OutOfScopeReason",
            "enum_values": [
              "social_insurance_case",
              "non_civil_case",
              "no_medical_malpractice",
              "wrong_claim_type",
              "labour_or_occupational_disease_case",
              "non_medical_personal_injury_case",
              "other",
              "not_applicable",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Główny powód uznania dokumentu za poza zakresem lub częściowo poza zakresem. Dla dokumentów w pełni relewantnych użyj not_applicable.",
            "name": "out_of_scope_reason"
          },
          {
            "type_": "enum",
            "enum_name": "OutOfScopeReasonSecondary",
            "enum_values": [
              "social_insurance_case",
              "non_civil_case",
              "no_medical_malpractice",
              "wrong_claim_type",
              "labour_or_occupational_disease_case",
              "non_medical_personal_injury_case",
              "other",
              "not_applicable",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Dodatkowy powód wyłączenia, gdy dokument spełnia więcej niż jedną kategorię poza zakresem.",
            "name": "out_of_scope_secondary_reason"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótkie uzasadnienie wyłączenia lub częściowego wyłączenia dokumentu, najlepiej w formie krótkiego cytatu albo streszczenia.",
            "name": "out_of_scope_reason_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "ProceedingType",
            "enum_values": [
              "civil_medical_malpractice",
              "social_insurance",
              "criminal",
              "administrative",
              "labour",
              "civil_labour_related_compensation",
              "labour_and_social_insurance_mixed",
              "other",
              "not_stated"
            ],
            "description": "Required: true. Typ: enum. Główny rodzaj postępowania. Używaj civil_medical_malpractice tylko gdy rdzeniem sprawy jest odpowiedzialność cywilna za leczenie, diagnozę, zabieg, poród lub opiekę medyczną.",
            "name": "proceeding_type"
          },
          {
            "type_": "enum",
            "enum_name": "ProceedingTypeSecondary",
            "enum_values": [
              "civil_medical_malpractice",
              "social_insurance",
              "criminal",
              "administrative",
              "labour",
              "civil_labour_related_compensation",
              "labour_and_social_insurance_mixed",
              "other",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Pomocnicza klasyfikacja rodzaju postępowania dla przypadków granicznych lub mieszanych.",
            "name": "proceeding_type_secondary"
          },
          {
            "type_": "enum",
            "enum_name": "DocumentFitForMeritsExtraction",
            "enum_values": [
              "good_fit",
              "limited_fit",
              "poor_fit",
              "out_of_scope"
            ],
            "description": "Required: true. Typ: enum. Ocena, czy dokument nadaje się do ekstrakcji meritum o czynnikach wpływających na kwoty. good_fit gdy uzasadnienie jest rozwinięte, limited_fit gdy część informacji da się wydobyć, poor_fit gdy dokument formalnie pasuje lecz jest zbyt skąpy, out_of_scope gdy sprawa jest poza zakresem.",
            "name": "document_fit_for_merits_extraction"
          },
          {
            "type_": "enum",
            "enum_name": "SourceCaseFamily",
            "enum_values": [
              "med_mal_civil",
              "social_insurance",
              "work_accident",
              "criminal_medical",
              "administrative_medical",
              "other"
            ],
            "description": "Required: true. Typ: enum. Rodzina sprawy przydatna do diagnostyki retrievalu i odróżniania spraw med-mal od podobnych spraw z innych reżimów.",
            "name": "source_case_family"
          },
          {
            "type_": "enum",
            "enum_name": "CourtLevel",
            "enum_values": [
              "district",
              "regional",
              "appellate",
              "supreme",
              "other",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Poziom sądu w strukturze sądownictwa. Ustal z nazwy sądu.",
            "name": "court_level"
          },
          {
            "type_": "enum",
            "enum_name": "CourtInstance",
            "enum_values": [
              "first_instance",
              "second_instance",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Instancja sądu, którego orzeczenie jest analizowane. Ustal z nagłówka, sentencji lub uzasadnienia.",
            "name": "court_instance"
          },
          {
            "type_": "enum",
            "enum_name": "ClaimContext",
            "enum_values": [
              "patient_direct_injury",
              "relative_claim_after_patient_death",
              "mixed",
              "other",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Podstawowy kontekst roszczenia: szkoda własna pacjenta albo roszczenia osób bliskich po śmierci pacjenta.",
            "name": "claim_context"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie występuje więcej niż jeden powód.",
            "name": "multiple_claimants_present"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: integer. Liczba powodów, jeśli da się ją ustalić jednoznacznie z dokumentu.",
            "name": "claimant_count"
          },
          {
            "type_": "enum",
            "enum_name": "ClaimantRolePrimary",
            "enum_values": [
              "patient",
              "spouse",
              "parent",
              "child",
              "sibling",
              "other_close_relative",
              "other",
              "mixed",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Rola głównego powoda albo dominującej grupy powodów.",
            "name": "claimant_role_primary"
          },
          {
            "type_": "enum",
            "enum_name": "ClaimAmountScope",
            "enum_values": [
              "per_claimant",
              "aggregate_for_all_claimants",
              "mixed_or_unclear",
              "not_applicable",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Zakres kwoty zadośćuczynienia w rekordzie: na osobę czy łącznie dla wszystkich powodów.",
            "name": "zadoscuczynienie_amount_scope"
          },
          {
            "type_": "enum",
            "enum_name": "ClaimAmountScope",
            "enum_values": [
              "per_claimant",
              "aggregate_for_all_claimants",
              "mixed_or_unclear",
              "not_applicable",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Zakres kwoty odszkodowania w rekordzie: na osobę czy łącznie dla wszystkich powodów.",
            "name": "odszkodowanie_amount_scope"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: integer. Wiek pacjenta w chwili zdarzenia medycznego, jeśli został podany wprost. Nie wnioskuj z anonimizacji.",
            "name": "patient_age"
          },
          {
            "type_": "enum",
            "enum_name": "PatientAgeGroup",
            "enum_values": [
              "infant",
              "child",
              "adolescent",
              "young_adult",
              "middle_aged",
              "older_adult",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Kategoria wieku pacjenta przydatna, gdy dokładny wiek nie jest ekstrahowalny.",
            "name": "patient_age_group"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy pacjent był małoletni w chwili zdarzenia.",
            "name": "patient_is_minor_at_event"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd wyraźnie potraktował wiek pacjenta jako czynnik wpływający na wysokość świadczenia.",
            "name": "patient_age_mentioned_as_amount_factor"
          },
          {
            "type_": "enum",
            "enum_name": "DefendantConfiguration",
            "enum_values": [
              "hospital_only",
              "insurer_only",
              "physician_only",
              "hospital_and_insurer",
              "hospital_and_physician",
              "insurer_and_physician",
              "multiple_mixed",
              "other",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Konfiguracja pozwanych w sprawie, szczególnie do porównań między szpitalem a ubezpieczycielem.",
            "name": "defendant_configuration"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Medyczny kontekst sprawy, np. specjalność, oddział lub rodzaj leczenia. Podaj krótki znormalizowany opis.",
            "name": "medical_specialty_or_treatment_context"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Opis procedury, zdarzenia lub etapu leczenia, którego dotyczy zarzut.",
            "name": "procedure_or_event_context"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sprawa dotyczy kontekstu okołoporodowego.",
            "name": "perinatal_context_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie występuje błąd diagnostyczny jako jedna z nieprawidłowości.",
            "name": "medical_error_type_diagnostic_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie występuje błąd terapeutyczny jako jedna z nieprawidłowości.",
            "name": "medical_error_type_therapeutic_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie występuje błąd techniczny, zabiegowy lub proceduralny jako jedna z nieprawidłowości.",
            "name": "medical_error_type_technical_procedural_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie występuje błąd organizacyjny jako jedna z nieprawidłowości.",
            "name": "medical_error_type_organizational_status"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Inny typ błędu medycznego niewygodny do zamknięcia w podstawowych kategoriach. Podaj krótki opis tylko gdy jest wyraźnie wskazany.",
            "name": "medical_error_type_other_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sprawa dotyczy opóźnienia diagnostyki lub leczenia jako elementu nieprawidłowości.",
            "name": "delay_in_diagnosis_or_treatment_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sprawa dotyczy braku lub wadliwości świadomej zgody pacjenta.",
            "name": "informed_consent_issue_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sprawa dotyczy zakażenia szpitalnego lub placówkowego.",
            "name": "hospital_acquired_infection_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sprawa dotyczy błędu w ordynacji, podaniu lub monitorowaniu leków.",
            "name": "medication_error_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sprawa dotyczy niewłaściwego monitorowania pacjenta albo zaniedbań opieki pooperacyjnej lub poleczeniowej.",
            "name": "monitoring_or_postoperative_care_failure_status"
          },
          {
            "type_": "enum",
            "enum_name": "ErrorConfirmedStatus",
            "enum_values": [
              "yes",
              "no",
              "partly_or_irregularity_only",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd stwierdził błąd medyczny albo równoważną nieprawidłowość.",
            "name": "error_confirmed_by_court"
          },
          {
            "type_": "enum",
            "enum_name": "CausalLinkStatus",
            "enum_values": [
              "confirmed",
              "rejected",
              "partial",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Status ustalenia związku przyczynowego między błędem a skutkiem zdrowotnym lub majątkowym.",
            "name": "causal_link_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd wyraźnie rozdzielił wpływ różnych przyczyn na skutek lub na wysokość świadczenia.",
            "name": "causal_contribution_split_explicit"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie tego, jak sąd opisał częściową kauzację, współprzyczyny lub podział wpływu różnych czynników.",
            "name": "causal_contribution_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "PatientOutcomeSeverity",
            "enum_values": [
              "temporary_consequences",
              "permanent_consequences",
              "death",
              "other_or_unclear",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Ogólna kategoria ciężaru skutków zdrowotnych opisana przez sąd.",
            "name": "patient_outcome_severity"
          },
          {
            "type_": "enum",
            "enum_name": "HealthImpairmentDurationType",
            "enum_values": [
              "permanent",
              "long_term",
              "both",
              "none_found",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Charakter uszczerbku na zdrowiu według sądu lub biegłego.",
            "name": "health_impairment_duration_type"
          },
          {
            "type_": "enum",
            "enum_name": "MentionAmountUseStatus",
            "enum_values": [
              "mentioned_and_used_for_amount",
              "mentioned_only",
              "not_mentioned",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy szczególnie nasilone cierpienia fizyczne zostały wskazane i czy sąd powiązał je z wysokością świadczenia. mentioned_and_used_for_amount tylko gdy z uzasadnienia wynika związek z miarkowaniem kwoty.",
            "name": "physical_suffering_severe_expressly_noted"
          },
          {
            "type_": "enum",
            "enum_name": "MentionAmountUseStatus",
            "enum_values": [
              "mentioned_and_used_for_amount",
              "mentioned_only",
              "not_mentioned",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy szczególnie nasilone cierpienia psychiczne zostały wskazane i czy sąd powiązał je z wysokością świadczenia.",
            "name": "psychological_suffering_severe_expressly_noted"
          },
          {
            "type_": "enum",
            "enum_name": "SufferingDurationCategory",
            "enum_values": [
              "short_term",
              "long_term",
              "permanent",
              "mixed_or_unclear",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Kategoria czasu trwania cierpień lub skutków krzywdy opisana w uzasadnieniu.",
            "name": "suffering_duration_category"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy skutki zdrowotne zostały uznane za nieodwracalne.",
            "name": "irreversible_effects_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd wskazał niekorzystne rokowania na przyszłość.",
            "name": "poor_prognosis_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd lub biegły opisał utratę szansy leczenia lub pogorszenie rokowań jako element szkody lub krzywdy.",
            "name": "loss_of_chance_or_worsened_prognosis_status"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie dotyczące utraty szansy leczenia lub pogorszenia rokowań.",
            "name": "loss_of_chance_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy stwierdzono trwałą niepełnosprawność albo trwałe istotne ograniczenie sprawności.",
            "name": "permanent_disability_status"
          },
          {
            "type_": "enum",
            "enum_name": "LossOfIndependenceStatus",
            "enum_values": [
              "yes",
              "partial",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy skutkiem była utrata samodzielności lub zależność od pomocy innych osób.",
            "name": "loss_of_independence_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy skutkiem było oszpecenie lub trwała zmiana wyglądu.",
            "name": "disfigurement_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd stwierdził przewlekły ból lub długotrwałe dolegliwości bólowe.",
            "name": "chronic_pain_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy skutki wymagają dalszego leczenia, rehabilitacji lub stałej opieki medycznej.",
            "name": "future_treatment_need_status"
          },
          {
            "type_": "enum",
            "enum_name": "ThirdPartyCareNeedStatus",
            "enum_values": [
              "temporary",
              "long_term",
              "permanent",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy skutki zdarzenia powodują potrzebę pomocy osób trzecich jako fakt medyczno-życiowy.",
            "name": "need_for_third_party_care_status"
          },
          {
            "type_": "enum",
            "enum_name": "MentionAmountUseStatus",
            "enum_values": [
              "mentioned_and_used_for_amount",
              "mentioned_only",
              "not_mentioned",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy wpływ skutków zdarzenia na życie rodzinne został wskazany i użyty jako argument kwotowy.",
            "name": "impact_on_family_life_status"
          },
          {
            "type_": "enum",
            "enum_name": "MentionAmountUseStatus",
            "enum_values": [
              "mentioned_and_used_for_amount",
              "mentioned_only",
              "not_mentioned",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy wpływ skutków zdarzenia na życie społeczne został wskazany i użyty jako argument kwotowy.",
            "name": "impact_on_social_life_status"
          },
          {
            "type_": "enum",
            "enum_name": "MentionAmountUseStatus",
            "enum_values": [
              "mentioned_and_used_for_amount",
              "mentioned_only",
              "not_mentioned",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy wpływ skutków zdarzenia na pracę, naukę lub aktywność zawodową został wskazany i użyty jako argument kwotowy.",
            "name": "impact_on_work_or_education_status"
          },
          {
            "type_": "enum",
            "enum_name": "MentionAmountUseStatus",
            "enum_values": [
              "mentioned_and_used_for_amount",
              "mentioned_only",
              "not_mentioned",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy wpływ skutków zdarzenia na codzienne funkcjonowanie został wskazany i użyty jako argument kwotowy.",
            "name": "impact_on_daily_functioning_status"
          },
          {
            "type_": "enum",
            "enum_name": "MentionAmountUseStatus",
            "enum_values": [
              "mentioned_and_used_for_amount",
              "mentioned_only",
              "not_mentioned",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy wpływ skutków zdarzenia na przyszłe plany życiowe lub jakość życia został wskazany i użyty jako argument kwotowy.",
            "name": "impact_on_future_life_plans_status"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w uzasadnieniu wskazano wielokrotne hospitalizacje, reoperacje albo powtarzalne interwencje medyczne jako element ciężaru krzywdy lub szkody.",
            "name": "repeated_hospitalization_or_reoperation_noted"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie wykorzystano opinię biegłego istotną dla rozstrzygnięcia.",
            "name": "expert_opinion_present"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Lista lub krótki opis specjalności biegłych istotnych dla sprawy.",
            "name": "expert_specialties_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "ExpertOpinionAdoption",
            "enum_values": [
              "fully_adopted",
              "partially_adopted",
              "rejected_or_mostly_rejected",
              "conflicting_no_clear_choice",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Jak sąd potraktował opinię biegłego przy ustaleniach faktycznych i ocenie roszczeń.",
            "name": "expert_opinion_adoption"
          },
          {
            "type_": "enum",
            "enum_name": "ExpertCausalSupport",
            "enum_values": [
              "yes",
              "no",
              "mixed_or_partial",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy opinia biegłego wspierała ustalenie związku przyczynowego między błędem a skutkiem.",
            "name": "expert_supported_causal_link"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy biegły podał procentowy uszczerbek na zdrowiu.",
            "name": "expert_provided_impairment_percent"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy w materiale występuje więcej niż jedna wartość procentowego uszczerbku na zdrowiu.",
            "name": "multiple_impairment_percent_values_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Wartość procentowego uszczerbku, którą sąd wybrał jako relewantną dla rozumowania o kwocie świadczenia. Wpisuj tylko gdy sąd tej wartości używa lub ją wyraźnie aprobuje.",
            "name": "court_relevant_health_impairment_percent"
          },
          {
            "type_": "enum",
            "enum_name": "HealthImpairmentPercentSource",
            "enum_values": [
              "expert_only",
              "court_explicitly_adopted",
              "conflicting_expert_values",
              "court_selected_from_conflicting_expert_values",
              "no_percent_given",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Źródło i status wartości procentowego uszczerbku. To pole dotyczy pochodzenia wartości, nie sposobu jej użycia w miarkowaniu.",
            "name": "health_impairment_percent_source"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki opis lub cytat pokazujący różne wartości procentowe uszczerbku, ich źródła i ewentualny wybór sądu.",
            "name": "health_impairment_percent_values_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy biegły odniósł się do rokowań na przyszłość.",
            "name": "expert_discussed_prognosis"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy występowały rozbieżności między opiniami biegłych lub między opinią a innymi dowodami.",
            "name": "expert_opinion_disagreement"
          },
          {
            "type_": "enum",
            "enum_name": "ExpertRoleInAmountReasoning",
            "enum_values": [
              "decisive",
              "important_but_not_decisive",
              "limited",
              "not_used_for_amount",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Znaczenie opinii biegłego dla samego miarkowania wysokości świadczenia.",
            "name": "expert_role_in_amount_reasoning"
          },
          {
            "type_": "enum",
            "enum_name": "CourtUsedImpairmentPercent",
            "enum_values": [
              "primary_basis",
              "important_auxiliary_factor",
              "minor_auxiliary_factor",
              "expressly_not_decisive",
              "no_percent_discussed",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Sposób wykorzystania procentowego uszczerbku przy ustalaniu kwoty zadośćuczynienia.",
            "name": "court_used_impairment_percent"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd wyraźnie zaznaczył, że wysokość zadośćuczynienia nie wynika mechanicznie z procentu uszczerbku albo że od tego procentu odchodzi.",
            "name": "court_explicitly_departed_from_impairment_percent"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie powodów, dla których sąd odszedł od prostego oparcia kwoty na procencie uszczerbku.",
            "name": "reasons_for_departure_from_impairment_percent_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy sąd wyraźnie wskazał konkretne czynniki decydujące o wysokości świadczenia.",
            "name": "court_explicitly_identified_amount_factors"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie najważniejszych czynników, które sąd uznał za decydujące dla wysokości zadośćuczynienia.",
            "name": "zadoscuczynienie_key_amount_factors_excerpt"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie najważniejszych czynników, które sąd uznał za decydujące dla wysokości odszkodowania.",
            "name": "odszkodowanie_key_amount_factors_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd potraktował poziom życia lub status majątkowy pacjenta albo powoda jako czynnik wpływający na wysokość świadczenia.",
            "name": "claimant_or_patient_living_standard_as_amount_factor"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie dotyczące poziomu życia lub sytuacji majątkowej pacjenta albo powoda jako argumentu kwotowego.",
            "name": "claimant_or_patient_living_standard_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd zastosował przyczynienie poszkodowanego przy obniżeniu świadczenia.",
            "name": "contributory_negligence_applied"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Procent przyczynienia poszkodowanego przyjęty przez sąd. Wpisuj tylko gdy wynika wprost z dokumentu.",
            "name": "contributory_negligence_percent"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy obniżenie świadczenia wynikało z przyczynienia poszkodowanego jako odrębnej przyczyny redukcji.",
            "name": "reduction_due_to_contributory_negligence"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy obniżenie świadczenia wynikało z częściowej kauzacji lub przypisania tylko części skutków błędowi medycznemu.",
            "name": "reduction_due_to_partial_causation"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy obniżenie lub oddalenie świadczenia wynikało z niedostatku dowodowego, np. niewykazania części kosztów lub rozmiaru szkody.",
            "name": "reduction_due_to_proof_deficit"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy obniżenie finalnej kwoty wynikało z zaliczenia wcześniejszej wypłaty w ramach tego samego zobowiązania.",
            "name": "reduction_due_to_pretrial_payment_offset"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd wskazał inny powód redukcji świadczenia niezwiązany bezpośrednio z rozmiarem krzywdy lub szkody.",
            "name": "reduction_due_to_other_non_harm_reason"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd uzasadniał wysokość zadośćuczynienia przez odwołanie do całokształtu indywidualnych okoliczności sprawy.",
            "name": "court_invoked_totality_of_circumstances"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd powołał funkcję kompensacyjną jako argument dla wysokości zadośćuczynienia.",
            "name": "court_invoked_compensatory_function"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd powołał przeciętną stopę życiową lub średni poziom życia społeczeństwa jako argument przy miarkowaniu kwoty.",
            "name": "court_invoked_average_living_standard"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd odwołał się do realiów ekonomicznych, wartości pieniądza, poziomu cen lub podobnych warunków ekonomicznych przy uzasadnianiu kwoty.",
            "name": "court_invoked_economic_conditions"
          },
          {
            "type_": "enum",
            "enum_name": "OtherJudgmentsReferenceLevel",
            "enum_values": [
              "none",
              "general_reference",
              "specific_cases",
              "specific_cases_and_amounts",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Poziom szczegółowości odwołania do innych orzeczeń przy uzasadnianiu odpowiedniości kwoty zadośćuczynienia.",
            "name": "zadoscuczynienie_referenced_other_judgments"
          },
          {
            "type_": "enum",
            "enum_name": "OtherJudgmentsReferenceMode",
            "enum_values": [
              "abstract_doctrinal_citation",
              "case_comparison_without_amounts",
              "case_comparison_with_amounts",
              "party_citation_only",
              "none",
              "mixed",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Tryb użycia innych orzeczeń. Rozróżnia cytowanie abstrakcyjnych tez od realnego porównywania konkretnych spraw i kwot.",
            "name": "other_judgments_reference_mode"
          },
          {
            "type_": "enum",
            "enum_name": "OtherJudgmentsReferenceSource",
            "enum_values": [
              "court_own_reasoning",
              "party_arguments_only",
              "both",
              "unclear",
              "not_applicable",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Źródło odwołania do innych orzeczeń: własne rozumowanie sądu, same twierdzenia stron lub oba.",
            "name": "other_judgments_reference_source"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie odwołań do innych orzeczeń, w tym sygnatur i kwot, jeśli są podane.",
            "name": "other_judgments_reference_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie pojawia się art. 444 k.c. jako podstawa roszczenia lub jego część.",
            "name": "legal_basis_art_444_kc_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie pojawia się art. 445 k.c. jako podstawa roszczenia lub jego część.",
            "name": "legal_basis_art_445_kc_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie pojawia się art. 446 § 4 k.c. jako podstawa roszczenia lub jego część.",
            "name": "legal_basis_art_446_4_kc_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie pojawia się art. 448 k.c. jako podstawa roszczenia lub jego część.",
            "name": "legal_basis_art_448_kc_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie pojawia się art. 430 k.c. jako podstawa odpowiedzialności lub jej część.",
            "name": "legal_basis_art_430_kc_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie pojawia się art. 415 k.c. jako podstawa odpowiedzialności lub jej część.",
            "name": "legal_basis_art_415_kc_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie pojawia się art. 822 k.c. jako podstawa odpowiedzialności ubezpieczyciela lub jej część.",
            "name": "legal_basis_art_822_kc_present"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Inna podstawa prawna niewygodna do zamknięcia w podstawowym słowniku. Podaj krótki opis przepisu lub kategorii.",
            "name": "legal_basis_other_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "ClaimPresentScoped",
            "enum_values": [
              "yes",
              "no",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie zgłoszono roszczenie o zadośćuczynienie.",
            "name": "zadoscuczynienie_claim_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota zadośćuczynienia pierwotnie dochodzona w pozwie lub przed zmianami powództwa, w PLN.",
            "name": "zadoscuczynienie_claimed_initial_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Końcowa kwota zadośćuczynienia dochodzona na moment wyrokowania w analizowanej instancji, w PLN.",
            "name": "zadoscuczynienie_claimed_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota bazowa zadośćuczynienia ustalona przez sąd przed redukcjami typu przyczynienie lub zaliczenie wcześniejszych świadczeń, w PLN. Wypełniaj tylko gdy sąd podaje tę bazę explicite; nie rekonstruuj jej z arytmetyki pośredniej.",
            "name": "zadoscuczynienie_base_amount_before_reductions_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota zadośćuczynienia po zastosowaniu offsetów lub zaliczeń, ale przed finalną kwotą zasądzoną, jeśli sąd pokazuje taki etap kalkulacji wprost. Nie wyliczaj samodzielnie.",
            "name": "zadoscuczynienie_amount_after_offsets_before_final_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Łączna kwota zadośćuczynienia zasądzona w analizowanym orzeczeniu, w PLN.",
            "name": "zadoscuczynienie_awarded_pln"
          },
          {
            "type_": "enum",
            "enum_name": "AwardOutcome",
            "enum_values": [
              "fully_awarded",
              "partly_awarded",
              "dismissed",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Wynik rozpoznania roszczenia o zadośćuczynienie.",
            "name": "zadoscuczynienie_award_outcome"
          },
          {
            "type_": "enum",
            "enum_name": "ClaimPresentScoped",
            "enum_values": [
              "yes",
              "no",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w sprawie zgłoszono roszczenie o odszkodowanie.",
            "name": "odszkodowanie_claim_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota odszkodowania pierwotnie dochodzona w pozwie lub przed zmianami powództwa, w PLN.",
            "name": "odszkodowanie_claimed_initial_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Końcowa kwota odszkodowania dochodzona na moment wyrokowania w analizowanej instancji, w PLN.",
            "name": "odszkodowanie_claimed_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota bazowa odszkodowania ustalona przed redukcjami typu przyczynienie lub zaliczenie świadczeń, w PLN. Wypełniaj tylko przy jawnej kalkulacji sądu; nie rekonstruuj.",
            "name": "odszkodowanie_base_amount_before_reductions_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota odszkodowania po zastosowaniu offsetów lub zaliczeń, ale przed finalną kwotą zasądzoną, jeśli sąd pokazuje taki etap kalkulacji wprost. Nie wyliczaj samodzielnie.",
            "name": "odszkodowanie_amount_after_offsets_before_final_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Łączna kwota odszkodowania zasądzona w analizowanym orzeczeniu, w PLN.",
            "name": "odszkodowanie_awarded_pln"
          },
          {
            "type_": "enum",
            "enum_name": "AwardOutcome",
            "enum_values": [
              "fully_awarded",
              "partly_awarded",
              "dismissed",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Wynik rozpoznania roszczenia o odszkodowanie.",
            "name": "odszkodowanie_award_outcome"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy przed wyrokiem doszło do wcześniejszej wypłaty świadczenia w ramach tego samego zobowiązania.",
            "name": "pretrial_payment_present"
          },
          {
            "type_": "enum",
            "enum_name": "PretrialPaymentPayerType",
            "enum_values": [
              "hospital_or_medical_entity",
              "insurer",
              "physician",
              "social_insurance_institution",
              "public_fund",
              "other_non_defendant_source",
              "other",
              "mixed",
              "not_applicable",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Źródło wcześniejszej wypłaty lub świadczenia omawianego przez sąd w kontekście finalnej kwoty.",
            "name": "pretrial_payment_payer_type"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota wcześniejszej wypłaty odnoszona do zadośćuczynienia, w PLN.",
            "name": "zadoscuczynienie_pretrial_payment_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota wcześniejszej wypłaty odnoszona do odszkodowania, w PLN.",
            "name": "odszkodowanie_pretrial_payment_pln"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd potraktował kwotę zasądzoną jako świadczenie uzupełniające po wcześniejszej wypłacie.",
            "name": "court_treated_award_as_supplementary"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy odszkodowanie obejmowało koszty lub straty już poniesione przed wyrokiem.",
            "name": "odszkodowanie_past_costs_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatus",
            "enum_values": [
              "yes",
              "no",
              "not_stated"
            ],
            "description": "Required: false. Typ: enum. Czy odszkodowanie obejmowało przyszłe koszty lub przyszłe straty majątkowe, bez renty.",
            "name": "odszkodowanie_future_costs_present"
          },
          {
            "type_": "enum",
            "enum_name": "OdszkodowanieCostsDocumentedStatus",
            "enum_values": [
              "fully_documented",
              "partly_documented",
              "insufficiently_documented",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Stopień udokumentowania kosztów dochodzonych w ramach odszkodowania.",
            "name": "odszkodowanie_costs_documented_status"
          },
          {
            "type_": "enum",
            "enum_name": "OdszkodowanieCostsAssessmentStatus",
            "enum_values": [
              "confirmed",
              "partly_confirmed",
              "rejected",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd uznał dochodzone koszty za konieczne i celowe.",
            "name": "odszkodowanie_costs_necessary_status"
          },
          {
            "type_": "enum",
            "enum_name": "OdszkodowanieCostsAssessmentStatus",
            "enum_values": [
              "confirmed",
              "partly_confirmed",
              "rejected",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy sąd uznał związek przyczynowy między konkretnymi kosztami lub stratami a błędem medycznym albo jego skutkami.",
            "name": "odszkodowanie_costs_causally_linked_status"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie powodów obniżenia lub oddalenia odszkodowania, np. brak dokumentów, brak konieczności wydatku, brak związku przyczynowego.",
            "name": "odszkodowanie_reduction_or_denial_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w materiale występuje kategoria kosztów leczenia w ramach odszkodowania.",
            "name": "treatment_costs_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w materiale występuje kategoria kosztów rehabilitacji w ramach odszkodowania.",
            "name": "rehabilitation_costs_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w materiale występuje kategoria kosztów opieki osób trzecich w ramach odszkodowania.",
            "name": "care_costs_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w materiale występuje kategoria kosztów dojazdów lub transportu w ramach odszkodowania.",
            "name": "travel_costs_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w materiale występuje kategoria utraconych zarobków lub dochodów w ramach odszkodowania.",
            "name": "lost_earnings_present"
          },
          {
            "type_": "enum",
            "enum_name": "BinaryStatusNA",
            "enum_values": [
              "yes",
              "no",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Czy w materiale występuje kategoria kosztów specjalnego żywienia lub odżywiania w ramach odszkodowania.",
            "name": "nutrition_costs_present"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Inne kategorie kosztów lub strat majątkowych objętych odszkodowaniem, niewyodrębnione w polach statusowych. Podaj krótki opis i ewentualnie kwoty, jeśli są wyraźnie wskazane.",
            "name": "other_odszkodowanie_costs_excerpt"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota zadośćuczynienia zasądzona przez sąd pierwszej instancji, jeśli jest znana z orzeczenia drugiej instancji lub akt.",
            "name": "first_instance_zadoscuczynienie_awarded_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Kwota odszkodowania zasądzona przez sąd pierwszej instancji, jeśli jest znana z orzeczenia drugiej instancji lub akt.",
            "name": "first_instance_odszkodowanie_awarded_pln"
          },
          {
            "type_": "enum",
            "enum_name": "AppealFiledBy",
            "enum_values": [
              "claimant",
              "defendant",
              "both",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Kto wniósł apelację istotną dla analizowanego orzeczenia. Dla orzeczeń pierwszej instancji użyj not_applicable.",
            "name": "appeal_filed_by"
          },
          {
            "type_": "enum",
            "enum_name": "AppealAmountScope",
            "enum_values": [
              "zadoscuczynienie_only",
              "odszkodowanie_only",
              "both",
              "other",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Jakiego zakresu dotyczyła apelacja w warstwie świadczeń pieniężnych.",
            "name": "appeal_amount_scope"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Zmiana kwoty zadośćuczynienia żądana w apelacji względem rozstrzygnięcia pierwszej instancji, jako liczba ze znakiem w PLN. Wypełniaj tylko gdy żądana zmiana wynika wprost z apelacji, uzasadnienia lub sentencji; nie wyliczaj pośrednio.",
            "name": "appeal_requested_zadoscuczynienie_change_pln"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: float. Zmiana kwoty odszkodowania żądana w apelacji względem rozstrzygnięcia pierwszej instancji, jako liczba ze znakiem w PLN. Wypełniaj tylko przy danych jawnych; nie wyliczaj pośrednio.",
            "name": "appeal_requested_odszkodowanie_change_pln"
          },
          {
            "type_": "enum",
            "enum_name": "AppellateChange",
            "enum_values": [
              "not_applicable",
              "upheld",
              "increased",
              "decreased",
              "vacated_or_remanded",
              "other_or_mixed"
            ],
            "description": "Required: false. Typ: enum. Sposób, w jaki sąd drugiej instancji potraktował kwotę zadośćuczynienia.",
            "name": "appellate_change_zadoscuczynienie"
          },
          {
            "type_": "enum",
            "enum_name": "AppellateChange",
            "enum_values": [
              "not_applicable",
              "upheld",
              "increased",
              "decreased",
              "vacated_or_remanded",
              "other_or_mixed"
            ],
            "description": "Required: false. Typ: enum. Sposób, w jaki sąd drugiej instancji potraktował kwotę odszkodowania.",
            "name": "appellate_change_odszkodowanie"
          },
          {
            "type_": "enum",
            "enum_name": "AppellateChangeReasonZ",
            "enum_values": [
              "reassessment_of_nonpecuniary_harm",
              "reassessment_of_expert_opinion",
              "causation_or_liability",
              "quantification_error",
              "insufficient_reasoning_of_first_instance",
              "mixed",
              "other",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Główny powód zmiany albo utrzymania kwoty zadośćuczynienia wskazany przez sąd odwoławczy. Jeśli motywy są wieloczynnikowe i sąd nie wskazuje wyraźnego priorytetu, użyj mixed albo not_stated zamiast sztucznego wyboru jednej przyczyny.",
            "name": "appellate_change_reason_zadoscuczynienie_primary"
          },
          {
            "type_": "enum",
            "enum_name": "AppellateChangeReasonO",
            "enum_values": [
              "pecuniary_damage_proof",
              "necessity_or_documentation_of_costs",
              "reassessment_of_expert_opinion",
              "causation_or_liability",
              "quantification_error",
              "insufficient_reasoning_of_first_instance",
              "mixed",
              "other",
              "not_stated",
              "not_applicable"
            ],
            "description": "Required: false. Typ: enum. Główny powód zmiany albo utrzymania kwoty odszkodowania wskazany przez sąd odwoławczy. Przy motywach mieszanych bez jednego priorytetu użyj mixed albo not_stated.",
            "name": "appellate_change_reason_odszkodowanie_primary"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie argumentów sądu drugiej instancji dotyczących zmiany lub utrzymania wysokości zadośćuczynienia.",
            "name": "appellate_change_reason_zadoscuczynienie_excerpt"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Required: false. Typ: string. Krótki cytat albo streszczenie argumentów sądu drugiej instancji dotyczących zmiany lub utrzymania wysokości odszkodowania.",
            "name": "appellate_change_reason_odszkodowanie_excerpt"
          }
        ]
        ```

=== "GPT-5.4 mini"

    **83 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `case_domain` | enum | Domain of the case established from the ruling's content — medical malpractice, another civil case, or undetermined. |
        | `is_medical_malpractice_case` | boolean | Whether the document concerns a medical-malpractice case and patient claims. Used as a quick domain filter. |
        | `medical_error_alleged_but_not_adjudicated` | boolean | Whether a medical error is alleged but not substantively ruled on by the court. |
        | `liability_found` | boolean | Whether the court found the defendant liable for the medical event or its consequences. |
        | `medical_error_found_by_court` | boolean | Whether the court explicitly found that a medical error occurred. |
        | `remedy_type` | enum | Which remedy is being analyzed in the ruling — compensation, damages, both, or a single combined amount. |
        | `claim_amounts_separated` | boolean | Whether the document clearly separates the compensation and damages amounts. |
        | `amount_claimed_total` | float | Total amount claimed by the plaintiff, if the document states a single sum or does not separate the claims. |
        | `amount_claimed_zadoscuczynienie` | float | Compensation amount claimed by the plaintiff, if the document clearly separates the claims. |
        | `amount_claimed_odszkodowanie` | float | Damages amount claimed by the plaintiff, if the document clearly separates the claims. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `case_domain` | enum | Domena sprawy ustalona na podstawie treści orzeczenia. Użyj `bled_medyczny`, gdy dokument dotyczy błędu medycznego i roszczeń pacjenta; `inna_sprawa_cywilna`, gdy sprawa nie jest medyczna; `nieustalone`, gdy nie da się tego potwierdzić. |
        | `is_medical_malpractice_case` | boolean | Czy dokument dotyczy sprawy o błąd medyczny i roszczenia pacjenta. Używaj jako szybkiego filtra domeny; powinno być spójne z `case_domain`. |
        | `medical_error_alleged_but_not_adjudicated` | boolean | Czy w dokumencie pojawia się zarzut błędu medycznego, ale sąd nie rozstrzyga go merytorycznie lub nie przesądza o nim wprost. Pomaga odróżnić zarzut strony od sądowego ustalenia. |
        | `liability_found` | boolean | Czy sąd ustalił odpowiedzialność pozwanego za zdarzenie medyczne lub jego skutki. Używaj tylko wtedy, gdy odpowiedzialność wynika wprost z sentencji albo uzasadnienia. |
        | `medical_error_found_by_court` | boolean | Czy sąd wprost stwierdził wystąpienie błędu medycznego. Nie myl z samym zarzutem strony; pole ma odzwierciedlać ustalenie sądu. |
        | `remedy_type` | enum | Jakie świadczenie jest analizowane w orzeczeniu. Użyj `jedna_laczna_kwota`, gdy dokument podaje jedną łączną kwotę bez wyraźnego rozbicia na zadośćuczynienie i odszkodowanie. |
        | `claim_amounts_separated` | boolean | Czy dokument wyraźnie rozdziela kwoty zadośćuczynienia i odszkodowania. Użyj `false`, gdy występuje tylko jedna łączna kwota lub rozbicie nie jest podane. |
        | `amount_claimed_total` | float | Łączna kwota dochodzona przez powoda, jeśli dokument podaje jedną sumę albo nie rozdziela roszczeń. Podawaj w złotych; gdy brak danych, pozostaw puste. |
        | `amount_claimed_zadoscuczynienie` | float | Kwota zadośćuczynienia dochodzona przez powoda, jeśli dokument wyraźnie rozdziela żądania. Jeśli podana jest tylko jedna łączna kwota, pozostaw puste i użyj `amount_claimed_total`. |
        | `amount_claimed_odszkodowanie` | float | Kwota odszkodowania dochodzona przez powoda, jeśli dokument wyraźnie rozdziela żądania. Jeśli podana jest tylko jedna łączna kwota, pozostaw puste i użyj `amount_claimed_total`. |
    ??? note "Show full schema (83 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "enum",
            "enum_name": "case_domain",
            "enum_values": [
              "bled_medyczny",
              "inna_sprawa_cywilna",
              "nieustalone"
            ],
            "description": "Domena sprawy ustalona na podstawie treści orzeczenia. Użyj `bled_medyczny`, gdy dokument dotyczy błędu medycznego i roszczeń pacjenta; `inna_sprawa_cywilna`, gdy sprawa nie jest medyczna; `nieustalone`, gdy nie da się tego potwierdzić.",
            "name": "case_domain"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dokument dotyczy sprawy o błąd medyczny i roszczenia pacjenta. Używaj jako szybkiego filtra domeny; powinno być spójne z `case_domain`.",
            "name": "is_medical_malpractice_case"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w dokumencie pojawia się zarzut błędu medycznego, ale sąd nie rozstrzyga go merytorycznie lub nie przesądza o nim wprost. Pomaga odróżnić zarzut strony od sądowego ustalenia.",
            "name": "medical_error_alleged_but_not_adjudicated"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd ustalił odpowiedzialność pozwanego za zdarzenie medyczne lub jego skutki. Używaj tylko wtedy, gdy odpowiedzialność wynika wprost z sentencji albo uzasadnienia.",
            "name": "liability_found"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost stwierdził wystąpienie błędu medycznego. Nie myl z samym zarzutem strony; pole ma odzwierciedlać ustalenie sądu.",
            "name": "medical_error_found_by_court"
          },
          {
            "type_": "enum",
            "enum_name": "remedy_type",
            "enum_values": [
              "zadośćuczynienie",
              "odszkodowanie",
              "oba",
              "jedna_laczna_kwota",
              "nieustalone"
            ],
            "description": "Jakie świadczenie jest analizowane w orzeczeniu. Użyj `jedna_laczna_kwota`, gdy dokument podaje jedną łączną kwotę bez wyraźnego rozbicia na zadośćuczynienie i odszkodowanie.",
            "name": "remedy_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dokument wyraźnie rozdziela kwoty zadośćuczynienia i odszkodowania. Użyj `false`, gdy występuje tylko jedna łączna kwota lub rozbicie nie jest podane.",
            "name": "claim_amounts_separated"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Łączna kwota dochodzona przez powoda, jeśli dokument podaje jedną sumę albo nie rozdziela roszczeń. Podawaj w złotych; gdy brak danych, pozostaw puste.",
            "name": "amount_claimed_total"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota zadośćuczynienia dochodzona przez powoda, jeśli dokument wyraźnie rozdziela żądania. Jeśli podana jest tylko jedna łączna kwota, pozostaw puste i użyj `amount_claimed_total`.",
            "name": "amount_claimed_zadoscuczynienie"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota odszkodowania dochodzona przez powoda, jeśli dokument wyraźnie rozdziela żądania. Jeśli podana jest tylko jedna łączna kwota, pozostaw puste i użyj `amount_claimed_total`.",
            "name": "amount_claimed_odszkodowanie"
          },
          {
            "type_": "enum",
            "enum_name": "claim_resolution_zadoscuczynienie_first_instance",
            "enum_values": [
              "uwzglednione_w_calosci",
              "uwzglednione_czesciowo",
              "oddalone_w_calosci",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Rozstrzygnięcie roszczenia o zadośćuczynienie w I instancji. Użyj `nie_dotyczy`, gdy roszczenie nie występuje; `nieustalone`, gdy brak jednoznacznej informacji. Nie stosuj tego pola do formalnego zakończenia sprawy bez meritum.",
            "name": "claim_resolution_zadoscuczynienie_first_instance"
          },
          {
            "type_": "enum",
            "enum_name": "award_status_zadoscuczynienie_first_instance",
            "enum_values": [
              "zasadzone",
              "czesciowo_zasadzone",
              "oddalone",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Status roszczenia o zadośćuczynienie w I instancji. Użyj `oddalone`, gdy świadczenie nie zostało zasądzone; w takim przypadku kwota może wynosić 0.0 tylko przy wprost oddalonym roszczeniu.",
            "name": "award_status_zadoscuczynienie_first_instance"
          },
          {
            "type_": "enum",
            "enum_name": "claim_resolution_zadoscuczynienie_final",
            "enum_values": [
              "uwzglednione_w_calosci",
              "uwzglednione_czesciowo",
              "oddalone_w_calosci",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Końcowe rozstrzygnięcie roszczenia o zadośćuczynienie w analizowanym orzeczeniu, zwykle po apelacji. Jeśli brak apelacji, zwykle odpowiada rozstrzygnięciu I instancji. Nie używaj jako opisu wyłącznie formalnego zakończenia sprawy.",
            "name": "claim_resolution_zadoscuczynienie_final"
          },
          {
            "type_": "enum",
            "enum_name": "award_status_zadoscuczynienie_final",
            "enum_values": [
              "zasadzone",
              "czesciowo_zasadzone",
              "oddalone",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Końcowy status roszczenia o zadośćuczynienie. Użyj `oddalone`, gdy finalnie nie zasądzono świadczenia; wtedy kwota może wynosić 0.0 tylko przy wprost oddalonym roszczeniu.",
            "name": "award_status_zadoscuczynienie_final"
          },
          {
            "type_": "enum",
            "enum_name": "claim_resolution_odszkodowanie_first_instance",
            "enum_values": [
              "uwzglednione_w_calosci",
              "uwzglednione_czesciowo",
              "oddalone_w_calosci",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Rozstrzygnięcie roszczenia o odszkodowanie w I instancji. Użyj `nie_dotyczy`, gdy roszczenie nie występuje; `nieustalone`, gdy brak jednoznacznej informacji. Nie stosuj do spraw zakończonych formalnie bez oceny meritum.",
            "name": "claim_resolution_odszkodowanie_first_instance"
          },
          {
            "type_": "enum",
            "enum_name": "award_status_odszkodowanie_first_instance",
            "enum_values": [
              "zasadzone",
              "czesciowo_zasadzone",
              "oddalone",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Status roszczenia o odszkodowanie w I instancji. Użyj `oddalone`, gdy świadczenie nie zostało zasądzone; w takim przypadku kwota może wynosić 0.0 tylko przy wprost oddalonym roszczeniu.",
            "name": "award_status_odszkodowanie_first_instance"
          },
          {
            "type_": "enum",
            "enum_name": "claim_resolution_odszkodowanie_final",
            "enum_values": [
              "uwzglednione_w_calosci",
              "uwzglednione_czesciowo",
              "oddalone_w_calosci",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Końcowe rozstrzygnięcie roszczenia o odszkodowanie w analizowanym orzeczeniu, zwykle po apelacji. Jeśli brak apelacji, zwykle odpowiada rozstrzygnięciu I instancji. Nie używaj jako opisu wyłącznie formalnego zakończenia sprawy.",
            "name": "claim_resolution_odszkodowanie_final"
          },
          {
            "type_": "enum",
            "enum_name": "award_status_odszkodowanie_final",
            "enum_values": [
              "zasadzone",
              "czesciowo_zasadzone",
              "oddalone",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Końcowy status roszczenia o odszkodowanie. Użyj `oddalone`, gdy finalnie nie zasądzono świadczenia; wtedy kwota może wynosić 0.0 tylko przy wprost oddalonym roszczeniu.",
            "name": "award_status_odszkodowanie_final"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Łączna kwota zasądzona w I instancji, jeśli dokument nie rozdziela świadczeń albo podaje jedną sumę. W przypadku formalnego zakończenia sprawy bez oceny meritum pozostaw puste.",
            "name": "amount_awarded_total_first_instance"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota zadośćuczynienia zasądzona w I instancji. Jeśli brak takiego rozstrzygnięcia, pozostaw puste; w przypadku wprost oddalonego roszczenia użyj 0.0.",
            "name": "amount_awarded_zadoscuczynienie_first_instance"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota odszkodowania zasądzona w I instancji. Jeśli brak takiego rozstrzygnięcia, pozostaw puste; w przypadku wprost oddalonego roszczenia użyj 0.0.",
            "name": "amount_awarded_odszkodowanie_first_instance"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Łączna kwota wynikająca z rozstrzygnięcia końcowego, jeśli dokument nie rozdziela świadczeń albo podaje jedną sumę. W przypadku formalnego zakończenia sprawy bez oceny meritum pozostaw puste.",
            "name": "amount_awarded_total_final"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Końcowa kwota zadośćuczynienia wynikająca z analizowanego orzeczenia po rozpoznaniu sprawy, także po apelacji. Jeśli brak rozbicia lub brak świadczenia, pozostaw puste albo użyj 0.0 przy wprost oddalonym roszczeniu.",
            "name": "amount_awarded_zadoscuczynienie_final"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Końcowa kwota odszkodowania wynikająca z analizowanego orzeczenia po rozpoznaniu sprawy, także po apelacji. Jeśli brak rozbicia lub brak świadczenia, pozostaw puste albo użyj 0.0 przy wprost oddalonym roszczeniu.",
            "name": "amount_awarded_odszkodowanie_final"
          },
          {
            "type_": "enum",
            "enum_name": "court_instance",
            "enum_values": [
              "I_instancja",
              "II_instancja",
              "nieustalone"
            ],
            "description": "Która instancja wydała analizowane orzeczenie. Użyj `II_instancja`, gdy dokument jest orzeczeniem sądu odwoławczego; `I_instancja`, gdy pochodzi z sądu pierwszej instancji.",
            "name": "court_instance"
          },
          {
            "type_": "enum",
            "enum_name": "appeal_outcome",
            "enum_values": [
              "utrzymano",
              "zmieniono",
              "uchylono",
              "oddalono",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Końcowy wynik postępowania apelacyjnego w sprawie. Użyj `nie_dotyczy`, gdy dokument nie dotyczy II instancji; `zmieniono`, gdy sąd odwoławczy zmienił rozstrzygnięcie; `utrzymano`, gdy je utrzymał; `oddalono`, gdy apelację oddalono.",
            "name": "appeal_outcome"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dokument w ogóle zawiera ocenę merytoryczną wysokości zadośćuczynienia lub odszkodowania. Użyj `false`, gdy sprawa kończy się przed oceną wysokości świadczenia.",
            "name": "case_decided_on_merits"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd w dokumencie ustala, miarkuje albo wprost ocenia konkretną kwotę świadczenia. Użyj `false`, gdy brak takiej oceny, nawet jeśli sprawa dotyczy roszczenia o zadośćuczynienie lub odszkodowanie.",
            "name": "amount_assessment_present"
          },
          {
            "type_": "enum",
            "enum_name": "procedural_disposition_reason",
            "enum_values": [
              "przedawnienie",
              "brak_legitymacji",
              "brak_wlasciwosci",
              "odrzucenie_pozwu",
              "umorzenie",
              "cofniecie_pozwu",
              "inne",
              "nieustalone",
              "nie_dotyczy"
            ],
            "description": "Główna przyczyna formalnego zakończenia sprawy, jeśli sąd nie doszedł do merytorycznej oceny świadczenia. Użyj tego pola dla barier procesowych, a nie dla materialnego oddalenia roszczenia.",
            "name": "procedural_disposition_reason"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd odwoławczy zmienił wysokość zadośćuczynienia. Stosuj tylko dla orzeczeń II instancji.",
            "name": "appellate_modified_zadoscuczynienie"
          },
          {
            "type_": "enum",
            "enum_name": "appellate_change_direction_zadoscuczynienie",
            "enum_values": [
              "podwyzszenie",
              "obnizenie",
              "bez_zmiany",
              "nieustalone",
              "nie_dotyczy"
            ],
            "description": "Kierunek zmiany kwoty zadośćuczynienia przez sąd odwoławczy. `podwyzszenie` albo `obnizenie`, gdy sąd zmienił kwotę; `bez_zmiany`, gdy ją utrzymano.",
            "name": "appellate_change_direction_zadoscuczynienie"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "O ile zmieniła się kwota zadośćuczynienia w II instancji względem kwoty sprzed zmiany. Podawaj jako dodatnią wartość w złotych, jeśli da się to ustalić.",
            "name": "appellate_change_amount_zadoscuczynienie"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd odwoławczy zmienił wysokość odszkodowania. Stosuj tylko dla orzeczeń II instancji.",
            "name": "appellate_modified_odszkodowanie"
          },
          {
            "type_": "enum",
            "enum_name": "appellate_change_direction_odszkodowanie",
            "enum_values": [
              "podwyzszenie",
              "obnizenie",
              "bez_zmiany",
              "nieustalone",
              "nie_dotyczy"
            ],
            "description": "Kierunek zmiany kwoty odszkodowania przez sąd odwoławczy. `podwyzszenie` albo `obnizenie`, gdy sąd zmienił kwotę; `bez_zmiany`, gdy ją utrzymano.",
            "name": "appellate_change_direction_odszkodowanie"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "O ile zmieniła się kwota odszkodowania w II instancji względem kwoty sprzed zmiany. Podawaj jako dodatnią wartość w złotych, jeśli da się to ustalić.",
            "name": "appellate_change_amount_odszkodowanie"
          },
          {
            "type_": "enum",
            "enum_name": "defendant_type",
            "enum_values": [
              "szpital",
              "podmiot_leczniczy_inny",
              "ubezpieczyciel",
              "lekarz",
              "mieszany",
              "inny",
              "nieustalone"
            ],
            "description": "Rodzaj pozwanego w sprawie. Użyj `mieszany`, gdy pozwanych jest kilku; gdy występuje zarówno szpital, jak i ubezpieczyciel, odnotuj to także w polach boolowskich dotyczących rodzaju pozwanego.",
            "name": "defendant_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy pozwanym lub jednym z pozwanych jest szpital. Ustaw na `true`, jeśli szpital występuje w sprawie jako strona pozwana.",
            "name": "defendant_is_hospital"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy pozwanym lub jednym z pozwanych jest ubezpieczyciel. Ustaw na `true`, jeśli ubezpieczyciel występuje w sprawie jako strona pozwana.",
            "name": "defendant_is_insurer"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy pozwanym lub jednym z pozwanych jest lekarz jako osoba fizyczna. Ustaw na `true`, jeśli lekarz występuje w sprawie jako strona pozwana.",
            "name": "defendant_is_physician"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy pozwanym lub jednym z pozwanych jest inny podmiot niż szpital, ubezpieczyciel lub lekarz, np. inny podmiot leczniczy albo jednostka organizacyjna.",
            "name": "defendant_is_other"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost odnosi status pozwanego do wysokości świadczenia lub sposobu uzasadnienia. Pomaga ocenić, czy różnica między szpitalem a ubezpieczycielem została wykorzystana w argumentacji.",
            "name": "defendant_status_discussed_in_reasoning"
          },
          {
            "type_": "enum",
            "enum_name": "medical_error_type",
            "enum_values": [
              "diagnostyczny",
              "terapeutyczny",
              "zabiegowy",
              "organizacyjny",
              "okoloporodowy",
              "zakazenie",
              "anestezjologiczny",
              "naruszenie_obowiazku_informacyjnego",
              "brak_zgody",
              "mieszany",
              "inny",
              "nieustalony"
            ],
            "description": "Główna kategoria błędu medycznego ustalona przez sąd. Jeśli orzeczenie łączy kilka typów, użyj `mieszany`; jeśli brak jednoznacznej kwalifikacji, użyj `nieustalony`. W sprawach formalnie zakończonych bez meritum dopuszczalne jest `nieustalony`.",
            "name": "medical_error_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w orzeczeniu występuje spór o zgodę pacjenta lub obowiązek informacyjny. Używaj, gdy dokument wprost dotyczy tej problematyki.",
            "name": "consent_issue_present"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost argumentuje, że pacjent i tak wyraziłby zgodę albo że wada informacyjna nie zmieniłaby decyzji pacjenta. Wychwytuje typowy argument o zgodzie hipotetycznej.",
            "name": "hypothetical_consent_argument_invoked"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wiek pacjenta w latach, jeśli został wskazany w orzeczeniu jako istotna okoliczność. Nie zgaduj wartości z opisu.",
            "name": "patient_age"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy pacjent zmarł w następstwie zdarzenia opisanego w sprawie. Używaj tylko wtedy, gdy z treści wynika zgon pacjenta jako skutek błędu medycznego.",
            "name": "patient_died"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w orzeczeniu wprost pojawia się procentowy uszczerbek na zdrowiu. Pole służy do odróżnienia spraw, w których ten wskaźnik w ogóle jest używany.",
            "name": "percent_health_impairment_present"
          },
          {
            "type_": "enum",
            "enum_name": "percent_health_impairment_source",
            "enum_values": [
              "biegly",
              "sąd",
              "oba",
              "brak",
              "nieustalone"
            ],
            "description": "Źródło procentowego uszczerbku na zdrowiu użytego w sprawie. Użyj `biegly`, gdy wartość pochodzi z opinii biegłego; `sąd`, gdy sąd sam przyjmuje wartość; `oba`, gdy występują oba źródła; `brak`, gdy wskaźnik nie występuje.",
            "name": "percent_health_impairment_source"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Procentowy uszczerbek na zdrowiu wskazany przez biegłego w I instancji, jeśli orzeczenie go podaje. Wartość numeryczna w procentach.",
            "name": "percent_health_impairment_expert_first_instance"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Procentowy uszczerbek na zdrowiu wskazany przez biegłego w rozstrzygnięciu końcowym. Wartość numeryczna w procentach, jeśli została wskazana.",
            "name": "percent_health_impairment_expert_final"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Procentowy uszczerbek na zdrowiu przyjęty przez sąd w I instancji. Jeśli sąd nie przyjmuje konkretnej wartości procentowej, pozostaw puste.",
            "name": "percent_health_impairment_adopted_by_court_first_instance"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Procentowy uszczerbek na zdrowiu przyjęty przez sąd w rozstrzygnięciu końcowym. Jeśli sąd nie przyjmuje konkretnej wartości procentowej, pozostaw puste.",
            "name": "percent_health_impairment_adopted_by_court_final"
          },
          {
            "type_": "enum",
            "enum_name": "percent_impairment_role_first_instance",
            "enum_values": [
              "glowna_podstawa",
              "jeden_z_elementow",
              "wspomniany_ale_nie_uzyty",
              "odrzucony",
              "nieustalony",
              "nie_dotyczy"
            ],
            "description": "Rola procentowego uszczerbku na zdrowiu w uzasadnieniu I instancji. Użyj `glowna_podstawa`, gdy sąd opiera kwotę wprost na tym wskaźniku; `nie_dotyczy`, gdy wskaźnik nie występuje.",
            "name": "percent_impairment_role_first_instance"
          },
          {
            "type_": "enum",
            "enum_name": "percent_impairment_role_final",
            "enum_values": [
              "glowna_podstawa",
              "jeden_z_elementow",
              "wspomniany_ale_nie_uzyty",
              "odrzucony",
              "nieustalony",
              "nie_dotyczy"
            ],
            "description": "Rola procentowego uszczerbku na zdrowiu w rozstrzygnięciu końcowym. Użyj `glowna_podstawa`, gdy sąd opiera kwotę wprost na tym wskaźniku; `nie_dotyczy`, gdy wskaźnik nie występuje.",
            "name": "percent_impairment_role_final"
          },
          {
            "type_": "enum",
            "enum_name": "expert_opinion_role",
            "enum_values": [
              "liability",
              "amount",
              "both",
              "none",
              "unknown"
            ],
            "description": "Jaką funkcję pełniła opinia biegłego w sprawie. Użyj `liability`, gdy decydowała o odpowiedzialności; `amount`, gdy przede wszystkim o wysokości świadczenia; `both`, gdy o obu kwestiach; `none`, gdy sąd jej nie wykorzystał.",
            "name": "expert_opinion_role"
          },
          {
            "type_": "enum",
            "enum_name": "expert_opinion_weight_first_instance",
            "enum_values": [
              "brak_opinii",
              "glowna_podstawa",
              "jeden_z_elementow",
              "drugorzedna",
              "pominieta",
              "nieustalone"
            ],
            "description": "Jaką wagę sąd przypisał opinii biegłego w I instancji przy ustalaniu odpowiedzialności lub wysokości świadczenia. Użyj `pominieta`, gdy opinia została dopuszczona, ale nie została realnie wykorzystana.",
            "name": "expert_opinion_weight_first_instance"
          },
          {
            "type_": "enum",
            "enum_name": "expert_opinion_weight_final",
            "enum_values": [
              "brak_opinii",
              "glowna_podstawa",
              "jeden_z_elementow",
              "drugorzedna",
              "pominieta",
              "nieustalone"
            ],
            "description": "Jaką wagę sąd przypisał opinii biegłego w rozstrzygnięciu końcowym przy ustalaniu odpowiedzialności lub wysokości świadczenia. Użyj `pominieta`, gdy opinia została dopuszczona, ale nie została realnie wykorzystana.",
            "name": "expert_opinion_weight_final"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd dopuścił i wykorzystał opinię biegłego w sprawie. Użyj `false`, gdy opinia nie została dopuszczona albo została pominięta w rozumowaniu sądu.",
            "name": "expert_opinion_admitted"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy strona wnioskowała o opinię biegłego, ale sąd jej nie dopuścił lub pominął ten dowód. Pole przydatne dla spraw, w których brak opinii wpływa na analizę miarkowania kwoty.",
            "name": "expert_opinion_requested_but_denied"
          },
          {
            "type_": "enum",
            "enum_name": "explicit_case_comparison",
            "enum_values": [
              "brak",
              "ogolne_odniesienie",
              "wprost_pojedyncze_orzeczenie",
              "wprost_wiele_orzeczen",
              "wprost_porownanie_kwot",
              "nieustalone"
            ],
            "description": "Czy sąd wprost porównuje sprawę z innymi orzeczeniami i w jakiej formie. Wybierz `wprost_porownanie_kwot`, gdy odnosi się bezpośrednio do wysokości kwot z innych spraw, a nie tylko cytuje orzecznictwo.",
            "name": "explicit_case_comparison"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost porównuje wysokość zasądzonych kwot z innymi sprawami, aby uzasadnić miarkowanie świadczenia. Używaj, gdy porównanie kwot jest jawne i funkcjonalne dla uzasadnienia.",
            "name": "direct_amount_benchmarking_present"
          },
          {
            "type_": "enum",
            "enum_name": "comparison_purpose",
            "enum_values": [
              "uzasadnienie_kwoty",
              "ustalenie_standardu",
              "odroznienie_sprawy",
              "inne",
              "nieustalone"
            ],
            "description": "Cel odwołania do innych orzeczeń, jeśli sąd takie porównanie zastosował. Użyj `uzasadnienie_kwoty`, gdy porównanie wspiera miarkowanie świadczenia.",
            "name": "comparison_purpose"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost odwołuje się do kompensacyjnej funkcji zadośćuczynienia lub odszkodowania.",
            "name": "compensation_function_invoked"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost odwołuje się do stopy życiowej społeczeństwa lub podobnego kryterium przy miarkowaniu kwoty.",
            "name": "living_standard_reference"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd akcentuje indywidualną ocenę krzywdy i okoliczności konkretnej sprawy jako element miarkowania świadczenia.",
            "name": "individualized_assessment_invoked"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w sprawie występuje więcej niż jeden istotny skutek błędu medycznego, np. ból i cierpienie oraz utrata samodzielności i potrzeba opieki.",
            "name": "harm_effects_mixed"
          },
          {
            "type_": "enum",
            "enum_name": "primary_harm_effect",
            "enum_values": [
              "bol_i_cierpienie",
              "trwale_ograniczenie_sprawnosci",
              "niepelnosprawnosc",
              "utrata_samodzielnosci",
              "potrzeba_opieki",
              "pogorszenie_zycia_rodzinnego",
              "pogorszenie_zycia_zawodowego",
              "szkoda_majatkowa",
              "zgon_pacjenta",
              "mieszane",
              "inne",
              "nieustalone"
            ],
            "description": "Najważniejsza kategoria skutku błędu medycznego ustalona przez sąd albo wynikająca z opisu stanu faktycznego. Jeśli skutki są wielorakie, użyj `mieszane`.",
            "name": "primary_harm_effect"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Czas trwania cierpień lub dolegliwości w miesiącach, jeśli da się go ustalić z orzeczenia. Nie zgaduj wartości.",
            "name": "suffering_duration_months"
          },
          {
            "type_": "enum",
            "enum_name": "suffering_intensity",
            "enum_values": [
              "niskie",
              "umiarkowane",
              "wysokie",
              "bardzo_wysokie",
              "nieustalone"
            ],
            "description": "Ocena intensywności cierpień fizycznych lub psychicznych opisywanych przez sąd. Używaj tylko wtedy, gdy uzasadnienie pozwala na taką klasyfikację.",
            "name": "suffering_intensity"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Średni dzienny zakres opieki osób trzecich nad pacjentem w godzinach, jeśli został wskazany w orzeczeniu. Jeśli sąd podaje zakres, przyjmij wartość średnią, o ile to zgodne z regułami ekstrakcji.",
            "name": "care_need_hours_per_day"
          },
          {
            "type_": "enum",
            "enum_name": "independence_loss_level",
            "enum_values": [
              "brak",
              "niski",
              "umiarkowany",
              "wysoki",
              "bardzo_wysoki",
              "nieustalony"
            ],
            "description": "Poziom utraty samodzielności pacjenta wynikającej ze skutków błędu medycznego. Uwzględnia ograniczenie codziennego funkcjonowania i zależność od osób trzecich.",
            "name": "independence_loss_level"
          },
          {
            "type_": "enum",
            "enum_name": "family_life_impact_level",
            "enum_values": [
              "brak",
              "niski",
              "umiarkowany",
              "wysoki",
              "bardzo_wysoki",
              "nieustalony"
            ],
            "description": "Poziom wpływu skutków błędu medycznego na życie rodzinne pacjenta. Uwzględnia trudności w relacjach rodzinnych i funkcjonowaniu domowym.",
            "name": "family_life_impact_level"
          },
          {
            "type_": "enum",
            "enum_name": "professional_life_impact_level",
            "enum_values": [
              "brak",
              "niski",
              "umiarkowany",
              "wysoki",
              "bardzo_wysoki",
              "nieustalony"
            ],
            "description": "Poziom wpływu skutków błędu medycznego na życie zawodowe lub zarobkowe pacjenta. Uwzględnia utratę zdolności do pracy i spadek dochodów.",
            "name": "professional_life_impact_level"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy skutki błędu medycznego były trwałe albo długotrwałe. Pomaga odróżnić skutki przemijające od takich, które zwykle zwiększają świadczenie.",
            "name": "effects_are_permanent_or_long_term"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wskazał wystąpienie niepełnosprawności pacjenta jako skutek błędu medycznego. Używaj tylko wtedy, gdy wynika to wprost lub jednoznacznie z uzasadnienia.",
            "name": "disability_present"
          },
          {
            "type_": "enum",
            "enum_name": "dismissal_reason_zadoscuczynienie",
            "enum_values": [
              "brak_winy",
              "brak_zwiazku_przyczynowego",
              "brak_szkody",
              "brak_dowodu",
              "przedawnienie",
              "brak_legitymacji",
              "inne",
              "nieustalone",
              "nie_dotyczy"
            ],
            "description": "Główna przyczyna materialnego oddalenia roszczenia o zadośćuczynienie, jeśli świadczenie nie zostało zasądzone albo zostało oddalone w części. Użyj `nie_dotyczy`, gdy roszczenie zostało uwzględnione. Nie stosuj do formalnego zakończenia sprawy bez meritum.",
            "name": "dismissal_reason_zadoscuczynienie"
          },
          {
            "type_": "enum",
            "enum_name": "dismissal_reason_odszkodowanie",
            "enum_values": [
              "brak_winy",
              "brak_zwiazku_przyczynowego",
              "brak_szkody",
              "brak_dowodu",
              "przedawnienie",
              "brak_legitymacji",
              "inne",
              "nieustalone",
              "nie_dotyczy"
            ],
            "description": "Główna przyczyna materialnego oddalenia roszczenia o odszkodowanie, jeśli świadczenie nie zostało zasądzone albo zostało oddalone w części. Użyj `nie_dotyczy`, gdy roszczenie zostało uwzględnione. Nie stosuj do formalnego zakończenia sprawy bez meritum.",
            "name": "dismissal_reason_odszkodowanie"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota kosztów leczenia lub innych wydatków medycznych uwzględnionych jako element odszkodowania, jeśli została wyodrębniona w orzeczeniu. Wartość w złotych.",
            "name": "medical_expenses_amount"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota kosztów rehabilitacji uwzględnionych jako element odszkodowania, jeśli została wyodrębniona w orzeczeniu. Wartość w złotych.",
            "name": "rehabilitation_expenses_amount"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota kosztów opieki osób trzecich uwzględnionych jako element odszkodowania, jeśli została wyodrębniona w orzeczeniu. Wartość w złotych.",
            "name": "care_expenses_amount"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota kosztów dojazdów lub transportu uwzględnionych jako element odszkodowania, jeśli została wyodrębniona w orzeczeniu. Wartość w złotych.",
            "name": "transport_expenses_amount"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota utraconych dochodów lub zarobków uwzględnionych jako element odszkodowania, jeśli została wyodrębniona w orzeczeniu. Wartość w złotych.",
            "name": "lost_income_amount"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Inne składniki szkody majątkowej uwzględnione przez sąd w odszkodowaniu, jeśli da się je wyodrębnić liczbowo. Wartość w złotych.",
            "name": "other_material_damage_amount"
          }
        ]
        ```

=== "Claude Sonnet 4.6"

    **62 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `czy_sprawa_dotyczy_bledu_medycznego` | boolean | Whether the analyzed document concerns a medical-malpractice case. Filtering field — fill in before extracting the remaining fields. |
        | `sygnatura_akt` | string | Case number of the court ruling — unique identifier needed for dataset management and deduplication. |
        | `rok_orzeczenia` | integer | Year the analyzed ruling was issued. |
        | `instancja_sadu` | enum | Instance and type of court that issued the ruling — first-instance regional court (high claim value), first-instance district court (low claim value), or appellate court as second instance. |
        | `identyfikator_sadu` | string | Name or identifier of the court that issued the ruling — enables grouping rulings by court or appellate district. |
        | `wydzial_sadu` | string | Division of the court that issued the ruling (e.g. civil, labor, commercial) — enables filtering to civil divisions. |
        | `rodzaj_pozwanego` | enum | Status of the defendant — physician as a natural person, hospital/medical entity, liability insurer, or a combination. |
        | `podmiot_leczniczy_publiczny_prywatny` | enum | Whether the defendant (or insured) medical entity is public or private. |
        | `typ_bledu_medycznego` | enum | Type of medical error underlying the claim — diagnostic, therapeutic/surgical, perinatal, pharmacological, anesthesiological, nursing, other. |
        | `kategoria_skutku_zdrowotnego` | enum | Category of health outcome resulting from the medical error. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `czy_sprawa_dotyczy_bledu_medycznego` | boolean | Czy analizowany dokument dotyczy sprawy o błąd medyczny (malpractice) — true jeśli przedmiotem sprawy jest roszczenie wynikające z działania lub zaniechania personelu medycznego; false jeśli dokument dotyczy innej domeny (np. wypadek komunikacyjny, błąd budowlany) nawet jeśli powołuje te same artykuły k.c. (art. 445 § 1, art. 444); pole filtrujące — wypełnić jako pierwsze przed ekstrakcją pozostałych pól |
        | `sygnatura_akt` | string | Sygnatura akt sprawy sądowej (np. 'I C 123/20') — unikalny identyfikator orzeczenia niezbędny do zarządzania zbiorem danych i deduplikacji |
        | `rok_orzeczenia` | integer | Rok wydania analizowanego orzeczenia (np. 2021) — standardowy atrybut zbioru danych sądowych; wymagany |
        | `instancja_sadu` | enum | Instancja i rodzaj sądu, który wydał analizowane orzeczenie; 'pierwsza_sad_okregowy' = sąd okręgowy orzekający jako I instancja (wysoki WPS); 'pierwsza_sad_rejonowy' = sąd rejonowy orzekający jako I instancja (niski WPS, np. roszczenia do 75 000 PLN); 'druga' = sąd apelacyjny jako II instancja; szukaj w nagłówku orzeczenia |
        | `identyfikator_sadu` | string | Nazwa lub identyfikator sądu, który wydał orzeczenie (np. 'Sąd Okręgowy w Warszawie' lub 'Sąd Apelacyjny w Krakowie') — umożliwia grupowanie orzeczeń według sądu lub okręgu apelacyjnego dla porównań międzysądowych; pole kluczowe dla Q7 i Q8 |
        | `wydzial_sadu` | string | Wydział sądu, który wydał orzeczenie (np. 'cywilny', 'pracy', 'gospodarczy') — umożliwia filtrowanie rekordów do wydziałów cywilnych oraz detekcję nieadekwatnych dokumentów (np. z wydziałów pracy) mogących zaburzyć analizy porównawcze; szukaj w nagłówku orzeczenia lub sygnaturze akt |
        | `rodzaj_pozwanego` | enum | Status pozwanego w sprawie — lekarz jako osoba fizyczna, szpital/podmiot leczniczy, ubezpieczyciel OC lub kombinacja; pole kluczowe dla Q5 |
        | `podmiot_leczniczy_publiczny_prywatny` | enum | Czy podmiot leczniczy będący pozwanym (lub ubezpieczany) jest podmiotem publicznym (SP ZOZ, jednostka samorządowa) czy prywatnym (spółka, praktyka prywatna); 'nieustalony' jeśli brak danych w orzeczeniu; pole kluczowe dla Q5 — może różnicować kwoty niezależnie od formalnego statusu pozwanego |
        | `typ_bledu_medycznego` | enum | Rodzaj błędu medycznego stanowiącego podstawę faktyczną roszczenia; 'diagnostyczny' = błąd w rozpoznaniu choroby; 'terapeutyczny_chirurgiczny' = błąd w leczeniu lub zabiegu chirurgicznym; 'okoloporodowy' = błąd podczas porodu lub opieki perinatalnej; 'farmakologiczny' = błąd w doborze lub dawkowaniu leku; 'anestezjologiczny' = błąd związany ze znieczuleniem; pole kluczowe dla Q3 |
        | `kategoria_skutku_zdrowotnego` | enum | Kategoria skutku zdrowotnego będącego następstwem błędu medycznego; pole kluczowe dla Q4 i Q10 |
    ??? note "Show full schema (62 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy analizowany dokument dotyczy sprawy o błąd medyczny (malpractice) — true jeśli przedmiotem sprawy jest roszczenie wynikające z działania lub zaniechania personelu medycznego; false jeśli dokument dotyczy innej domeny (np. wypadek komunikacyjny, błąd budowlany) nawet jeśli powołuje te same artykuły k.c. (art. 445 § 1, art. 444); pole filtrujące — wypełnić jako pierwsze przed ekstrakcją pozostałych pól",
            "name": "czy_sprawa_dotyczy_bledu_medycznego"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Sygnatura akt sprawy sądowej (np. 'I C 123/20') — unikalny identyfikator orzeczenia niezbędny do zarządzania zbiorem danych i deduplikacji",
            "name": "sygnatura_akt"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Rok wydania analizowanego orzeczenia (np. 2021) — standardowy atrybut zbioru danych sądowych; wymagany",
            "name": "rok_orzeczenia"
          },
          {
            "type_": "enum",
            "enum_name": "InstancjaSadu",
            "enum_values": [
              "pierwsza_sad_okregowy",
              "pierwsza_sad_rejonowy",
              "druga"
            ],
            "description": "Instancja i rodzaj sądu, który wydał analizowane orzeczenie; 'pierwsza_sad_okregowy' = sąd okręgowy orzekający jako I instancja (wysoki WPS); 'pierwsza_sad_rejonowy' = sąd rejonowy orzekający jako I instancja (niski WPS, np. roszczenia do 75 000 PLN); 'druga' = sąd apelacyjny jako II instancja; szukaj w nagłówku orzeczenia",
            "name": "instancja_sadu"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Nazwa lub identyfikator sądu, który wydał orzeczenie (np. 'Sąd Okręgowy w Warszawie' lub 'Sąd Apelacyjny w Krakowie') — umożliwia grupowanie orzeczeń według sądu lub okręgu apelacyjnego dla porównań międzysądowych; pole kluczowe dla Q7 i Q8",
            "name": "identyfikator_sadu"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Wydział sądu, który wydał orzeczenie (np. 'cywilny', 'pracy', 'gospodarczy') — umożliwia filtrowanie rekordów do wydziałów cywilnych oraz detekcję nieadekwatnych dokumentów (np. z wydziałów pracy) mogących zaburzyć analizy porównawcze; szukaj w nagłówku orzeczenia lub sygnaturze akt",
            "name": "wydzial_sadu"
          },
          {
            "type_": "enum",
            "enum_name": "RodzajPozwanego",
            "enum_values": [
              "lekarz_osoba_fizyczna",
              "szpital_podmiot_leczniczy",
              "ubezpieczyciel_oc",
              "szpital_i_ubezpieczyciel_solidarnie",
              "inny_lub_kilku"
            ],
            "description": "Status pozwanego w sprawie — lekarz jako osoba fizyczna, szpital/podmiot leczniczy, ubezpieczyciel OC lub kombinacja; pole kluczowe dla Q5",
            "name": "rodzaj_pozwanego"
          },
          {
            "type_": "enum",
            "enum_name": "PodmiotLeczniczyPublicznyPrywatny",
            "enum_values": [
              "publiczny",
              "prywatny",
              "nieustalony"
            ],
            "description": "Czy podmiot leczniczy będący pozwanym (lub ubezpieczany) jest podmiotem publicznym (SP ZOZ, jednostka samorządowa) czy prywatnym (spółka, praktyka prywatna); 'nieustalony' jeśli brak danych w orzeczeniu; pole kluczowe dla Q5 — może różnicować kwoty niezależnie od formalnego statusu pozwanego",
            "name": "podmiot_leczniczy_publiczny_prywatny"
          },
          {
            "type_": "enum",
            "enum_name": "TypBleduMedycznego",
            "enum_values": [
              "diagnostyczny",
              "terapeutyczny_chirurgiczny",
              "okoloporodowy",
              "farmakologiczny",
              "anestezjologiczny",
              "blad_pielegnacyjny",
              "inny",
              "nieustalony"
            ],
            "description": "Rodzaj błędu medycznego stanowiącego podstawę faktyczną roszczenia; 'diagnostyczny' = błąd w rozpoznaniu choroby; 'terapeutyczny_chirurgiczny' = błąd w leczeniu lub zabiegu chirurgicznym; 'okoloporodowy' = błąd podczas porodu lub opieki perinatalnej; 'farmakologiczny' = błąd w doborze lub dawkowaniu leku; 'anestezjologiczny' = błąd związany ze znieczuleniem; pole kluczowe dla Q3",
            "name": "typ_bledu_medycznego"
          },
          {
            "type_": "enum",
            "enum_name": "KategoriaSkutkuZdrowotnego",
            "enum_values": [
              "smierc_pacjenta",
              "trwale_kalectwo_znaczne",
              "trwaly_uszczerbek_mniejszy",
              "tymczasowy_uszczerbek",
              "wielorakie_skutki_mieszane"
            ],
            "description": "Kategoria skutku zdrowotnego będącego następstwem błędu medycznego; pole kluczowe dla Q4 i Q10",
            "name": "kategoria_skutku_zdrowotnego"
          },
          {
            "type_": "enum",
            "enum_name": "PodmiotRoszczacy",
            "enum_values": [
              "pacjent",
              "osoby_bliskie_po_smierci",
              "pacjent_i_osoby_bliskie"
            ],
            "description": "Kto dochodzi roszczenia — sam pacjent czy osoby bliskie (np. na podstawie art. 446 § 4 k.c.) po śmierci pacjenta; pole kluczowe dla Q10",
            "name": "podmiot_roszczacy"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba powodów w sprawie (osób dochodzących roszczeń) — w sprawach z art. 446 § 4 k.c. często jest kilku powodów (członkowie rodziny), co wpływa na kwoty indywidualne; wartość 1 dla pojedynczego powoda; pole kluczowe dla Q10",
            "name": "liczba_powodow"
          },
          {
            "type_": "enum",
            "enum_name": "StopienUwzglednieniaPowodztwa",
            "enum_values": [
              "w_calosci",
              "czesciowo",
              "oddalone"
            ],
            "description": "Stopień uwzględnienia powództwa przez sąd — 'w_calosci' jeśli zasądzono pełną żądaną kwotę, 'czesciowo' jeśli zasądzono część, 'oddalone' jeśli powództwo zostało w całości oddalone; zmienna zależna ułatwiająca filtrowanie spraw",
            "name": "stopien_uwzglednienia_powodztwa"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota zadośćuczynienia żądana przez powoda w PLN; wartość 0 jeśli roszczenie o zadośćuczynienie nie było dochodzone",
            "name": "kwota_zadoscuczynienia_zadana"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota zadośćuczynienia zasądzona przez sąd w PLN; wartość 0 jeśli powództwo w tym zakresie zostało oddalone",
            "name": "kwota_zadoscuczynienia_zasadzona"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota zewnętrznych świadczeń (np. wypłaconych przez ubezpieczyciela przed procesem, ZUS, inne podmioty) odliczona przez sąd od należnego zadośćuczynienia przy ustalaniu kwoty zasądzonej; wartość 0 jeśli sąd nie dokonał odliczeń lub brak informacji o odliczeniach; pole istotne dla prawidłowej interpretacji kwoty netto zasądzonej w kontekście modeli predykcyjnych Q1, Q2, Q5",
            "name": "swiadczenia_zaliczone_na_poczet_zadoscuczynienia"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Minimalna kwota zadośćuczynienia zasądzona na jednego powoda w PLN — w sprawach wieloosobowych (liczba_powodow > 1) pozwala uchwycić rozpiętość kwot indywidualnych; równa kwocie zasądzonej dla pojedynczego powoda; pole kluczowe dla Q10",
            "name": "kwota_zadoscuczynienia_na_powoda_min"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Maksymalna kwota zadośćuczynienia zasądzona na jednego powoda w PLN — w sprawach wieloosobowych (liczba_powodow > 1) pozwala uchwycić rozpiętość kwot indywidualnych; równa kwocie zasądzonej dla pojedynczego powoda; pole kluczowe dla Q10",
            "name": "kwota_zadoscuczynienia_na_powoda_max"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota zadośćuczynienia zasądzona przez sąd I instancji w PLN — uzupełniać wyłącznie dla orzeczeń sądu II instancji; wartość 0 jeśli sąd I instancji oddalił powództwo; pole 'kwota_zadoscuczynienia_i_instancji_znana' wskazuje, czy wartość jest dostępna; pole kluczowe dla Q6",
            "name": "kwota_zadoscuczynienia_sad_i_instancji"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy kwota zadośćuczynienia zasądzona przez sąd I instancji jest znana i dostępna w analizowanym orzeczeniu; false dla orzeczeń sądu I instancji lub gdy kwota I instancji nie jest podana w uzasadnieniu; pole pomocnicze dla 'kwota_zadoscuczynienia_sad_i_instancji'",
            "name": "kwota_zadoscuczynienia_i_instancji_znana"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota odszkodowania żądana przez powoda w PLN (szkoda majątkowa z art. 444 § 1 k.c.); wartość 0 jeśli roszczenie o odszkodowanie nie było dochodzone",
            "name": "kwota_odszkodowania_zadana"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota odszkodowania zasądzonego przez sąd w PLN (szkoda majątkowa z art. 444 § 1 k.c.); wartość 0 jeśli powództwo w tym zakresie zostało oddalone",
            "name": "kwota_odszkodowania_zasadzona"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota odszkodowania zasądzona przez sąd I instancji w PLN (art. 444 § 1 k.c.) — uzupełniać wyłącznie dla orzeczeń sądu II instancji; wartość 0 jeśli sąd I instancji oddalił powództwo; pole 'kwota_odszkodowania_i_instancji_znana' wskazuje, czy wartość jest dostępna; pole kluczowe dla Q6",
            "name": "kwota_odszkodowania_sad_i_instancji"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy kwota odszkodowania zasądzona przez sąd I instancji jest znana i dostępna w analizowanym orzeczeniu; false dla orzeczeń sądu I instancji lub gdy kwota I instancji nie jest podana w uzasadnieniu; pole pomocnicze dla 'kwota_odszkodowania_sad_i_instancji'",
            "name": "kwota_odszkodowania_i_instancji_znana"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wiek poszkodowanego pacjenta w chwili zdarzenia (błędu medycznego) w pełnych latach; wartość 0 jeśli wiek_ustalony=false; pole 'wiek_ustalony' wskazuje, czy wartość jest rzeczywiście dostępna; pole kluczowe dla Q1",
            "name": "wiek_poszkodowanego"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wiek poszkodowanego pacjenta w chwili zdarzenia został ustalony w sprawie i jest dostępny w orzeczeniu; false jeśli wiek nie wynika z uzasadnienia; pole pomocnicze dla 'wiek_poszkodowanego'",
            "name": "wiek_ustalony"
          },
          {
            "type_": "enum",
            "enum_name": "RodzajUszczerbkuNaZdrowiu",
            "enum_values": [
              "trwaly",
              "dlugotrwaly",
              "oba",
              "nieustalony"
            ],
            "description": "Rodzaj uszczerbku na zdrowiu ustalony przez biegłego lub wskazany przez sąd; 'trwaly' = uszczerbek nierokujący poprawy (trwałe naruszenie sprawności organizmu); 'dlugotrwaly' = uszczerbek powyżej 6 miesięcy, który może ustąpić; 'oba' = sprawa zawiera oba rodzaje; 'nieustalony' = brak wyraźnego rozróżnienia w orzeczeniu; pole towarzyszące 'procentowy_uszczerbek_na_zdrowiu' — zapobiega błędnej klasyfikacji długotrwałego uszczerbku jako trwałego; pole kluczowe dla Q2",
            "name": "rodzaj_uszczerbku_na_zdrowiu"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Procentowy trwały uszczerbek na zdrowiu ustalony przez biegłego sądowego (0–100); wartość 0 jeśli uszczerbek_procentowy_ustalony=false; pole 'uszczerbek_procentowy_ustalony' wskazuje, czy biegły rzeczywiście określił wskaźnik procentowy; interpretować łącznie z 'rodzaj_uszczerbku_na_zdrowiu'; pole kluczowe dla Q2",
            "name": "procentowy_uszczerbek_na_zdrowiu"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy biegły sądowy ustalił procentowy wskaźnik uszczerbku na zdrowiu w tej sprawie; false jeśli opinia biegłego nie zawiera procentowego określenia uszczerbku; pole pomocnicze dla 'procentowy_uszczerbek_na_zdrowiu'",
            "name": "uszczerbek_procentowy_ustalony"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost oparł wysokość kwoty zadośćuczynienia na procentowym wskaźniku uszczerbku stosując mechaniczny przelicznik (np. 'x PLN za 1% uszczerbku') lub wyraźnie deklaruje, że procent uszczerbku jest bezpośrednią podstawą wyliczenia kwoty — true wyłącznie w tych przypadkach; samo wymienienie procentu uszczerbku w uzasadnieniu obok innych okoliczności NIE jest wystarczające do oznaczenia true; pole kluczowe dla Q2",
            "name": "sad_oparl_kwote_na_wskazniku_uszczerbku"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wyraźnie wyszedł poza procentowy wskaźnik uszczerbku, wskazując dodatkowe przesłanki uzasadniające wyższą lub niższą kwotę (np. wyjątkowe cierpienia, szczególny wpływ na życie, młody wiek); pole kluczowe dla Q2",
            "name": "sad_wyszedl_poza_wskaznik_uszczerbku"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd uznał opinię biegłego sądowego za kluczowy dowód przesądzający o wysokości zasądzonej kwoty (tj. sąd expressis verbis powiązał swoje rozstrzygnięcie z wnioskami biegłego); pole kluczowe dla Q2",
            "name": "opinia_bieglego_decydujaca_dla_kwoty"
          },
          {
            "type_": "enum",
            "enum_name": "RokowaniaZdrowotne",
            "enum_values": [
              "pozytywne",
              "negatywne",
              "mieszane",
              "nieustalone"
            ],
            "description": "Rokowania zdrowotne poszkodowanego ustalone przez biegłego sądowego lub wskazane przez sąd — pozytywne (poprawa stanu zdrowia możliwa), negatywne (stan nierokujący poprawy lub prognoza pogorszenia), mieszane (częściowa poprawa), nieustalone (brak wyraźnego stanowiska w sprawie); sądy powołują się na rokowania jako odrębną okoliczność miarkowania; pole kluczowe dla Q1 i Q2",
            "name": "rokowania_zdrowotne"
          },
          {
            "type_": "enum",
            "enum_name": "IntensywnoscCierpien",
            "enum_values": [
              "niska",
              "srednia",
              "wysoka",
              "bardzo_wysoka",
              "nieustalona"
            ],
            "description": "Intensywność cierpień fizycznych i psychicznych poszkodowanego w ocenie sądu; 'niska' = nieznaczny dyskomfort, krótkotrwały ból bez trwałych następstw; 'srednia' = umiarkowany ból wymagający leczenia farmakologicznego lub rehabilitacji; 'wysoka' = silny ból wymagający długotrwałego leczenia, ograniczający codzienne funkcjonowanie; 'bardzo_wysoka' = bardzo silny ból wymagający opioidów lub całkowita niezdolność do samodzielnego funkcjonowania; 'nieustalona' = sąd nie wypowiada się na temat intensywności cierpień; pole kluczowe dla Q1",
            "name": "intensywnosc_cierpien"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Czas trwania cierpień poszkodowanego w miesiącach według ustaleń sądu (zaokrąglony do pełnych miesięcy); wartość 0 jeśli czas_cierpien_ustalony=false lub cierpienia mają charakter trwały (cierpienia_trwale=true); pole 'czas_cierpien_ustalony' wskazuje, czy wartość jest rzeczywiście dostępna; pole kluczowe dla Q1",
            "name": "czas_trwania_cierpien_miesiac"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy czas trwania cierpień poszkodowanego został ustalony w sprawie jako skończona wielkość wyrażona liczbowo (możliwa konwersja na miesiące); false jeśli czas nie został określony liczbowo lub cierpienia mają charakter trwały (wówczas 'cierpienia_trwale'=true); pole pomocnicze dla 'czas_trwania_cierpien_miesiac'",
            "name": "czas_cierpien_ustalony"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd ustalił, że cierpienia poszkodowanego mają charakter trwały lub bezterminowy (nie rokują ustąpienia); pozwala odróżnić cierpienia permanentne od przypadku, w którym czas trwania był po prostu nieustalony; pole kluczowe dla Q1",
            "name": "cierpienia_trwale"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd ustalił, że skutki błędu medycznego są nieodwracalne (trwałe, niemożliwe do wyleczenia lub naprawienia); pole kluczowe dla Q1",
            "name": "nieodwracalnosc_skutkow"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wskazał utratę lub istotne ograniczenie samodzielności poszkodowanego jako okoliczność wpływającą na wysokość kwoty; pole kluczowe dla Q1",
            "name": "utrata_samodzielnosci"
          },
          {
            "type_": "enum",
            "enum_name": "StopienNiepelnosprawnosci",
            "enum_values": [
              "brak",
              "lekki",
              "umiarkowany",
              "znaczny",
              "nieustalony"
            ],
            "description": "Stopień niepełnosprawności orzeczony lub ustalony przez sąd w sprawie (zgodnie z orzeczeniem o niepełnosprawności lub oceną sądu); pole kluczowe dla Q1",
            "name": "stopien_niepelnosprawnosci"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wskazał negatywny wpływ na życie zawodowe poszkodowanego (utrata lub istotne ograniczenie zdolności do pracy) jako okoliczność uwzględnioną przy miarkowaniu kwoty; pole kluczowe dla Q1",
            "name": "wplyw_na_zycie_zawodowe"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wskazał negatywny wpływ na życie rodzinne poszkodowanego jako okoliczność uwzględnioną przy miarkowaniu kwoty; pole kluczowe dla Q1",
            "name": "wplyw_na_zycie_rodzinne"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd uwzględnił przyczynienie się poszkodowanego do powstania lub zwiększenia szkody (art. 362 k.c.) i obniżył zasądzone świadczenie o ustalony procent przyczynienia; pole kluczowe dla predykcji kwot",
            "name": "sad_uwzglednil_przyczynienie"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd faktycznie obniżył zasądzoną kwotę z powodu przyczynienia — true wyłącznie gdy redukcja kwoty wynika wprost z przyczynienia; odróżnia przypadki gdy sąd stwierdza przyczynienie ale nie obniża kwoty (false) od przypadków faktycznej redukcji (true); uzupełniać tylko gdy sad_uwzglednil_przyczynienie=true; pole pomocnicze zapobiegające błędnej interpretacji pary sad_uwzglednil_przyczynienie=true + procent=0",
            "name": "przyczynienie_wplywa_na_kwote"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Procentowy stopień przyczynienia się poszkodowanego do powstania lub zwiększenia szkody ustalony przez sąd (0–100); wartość 0 jeśli sąd nie uwzględnił przyczynienia lub przyczynienie opisano wyłącznie jakościowo (wtedy uzupełnij 'przyczynienie_opis_jakosciowy'); pole kluczowe dla predykcji kwot",
            "name": "przyczynienie_poszkodowanego_procent"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Jakościowy opis przyczynienia poszkodowanego gdy sąd nie podał wartości procentowej — np. 'znikome', 'nieznaczne', 'minimalne', 'znaczne'; pozostawić puste jeśli sąd podał wartość procentową lub nie stwierdził przyczynienia; pole kluczowe gdy sad_uwzglednil_przyczynienie=true a przyczynienie_poszkodowanego_procent=0",
            "name": "przyczynienie_opis_jakosciowy"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Procentowy stopień przyczynienia się poszkodowanego ustalony przez sąd I instancji (0–100) — uzupełniać wyłącznie dla orzeczeń sądu II instancji, gdy sąd apelacyjny zmienił wartość przyczynienia względem I instancji lub gdy wartość przyczynienia z I instancji jest podana w uzasadnieniu; wartość 0 jeśli sąd I instancji nie uwzględnił przyczynienia; pole kluczowe dla Q6",
            "name": "przyczynienie_procent_sad_i_instancji"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost odwołał się do innych orzeczeń sądowych (wyroków) przy uzasadnianiu przyjętej kwoty zadośćuczynienia (choćby ogólnie); pole kluczowe dla Q7",
            "name": "sad_porownuje_do_innych_wyrokow"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd przytacza konkretne sygnatury akt lub kwoty z innych spraw (porównanie wprost), a nie jedynie ogólne stwierdzenia o orzecznictwie; pole kluczowe dla Q7",
            "name": "sad_porownuje_wprost_z_sygnaturami"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd explicite odwołuje się do funkcji kompensacyjnej zadośćuczynienia (przywrócenie równowagi naruszonej przez krzywdę, pełna kompensata niemajątkowego uszczerbku) w uzasadnieniu; pole kluczowe dla Q8",
            "name": "sad_odwoluje_sie_do_funkcji_kompensacyjnej"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd odwołuje się do funkcji satysfakcjonującej zadośćuczynienia — tj. celu polegającego na przyniesieniu poszkodowanemu poczucia ulgi, złagodzenia doznanej krzywdy i moralnego zadośćuczynienia — bez utożsamiania z funkcją represyjną; pole kluczowe dla Q8",
            "name": "sad_odwoluje_sie_do_funkcji_satysfakcjonujacej"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd odwołuje się do kryterium stopy życiowej społeczeństwa (przeciętny poziom życia w kraju) przy miarkowaniu kwoty; pole kluczowe dla Q8",
            "name": "sad_odwoluje_sie_do_stopy_zyciowej"
          },
          {
            "type_": "enum",
            "enum_name": "ZmianaKwotyApelacja",
            "enum_values": [
              "podwyzszenie",
              "obnizenie",
              "brak_zmiany",
              "nie_dotyczy"
            ],
            "description": "Kierunek zmiany kwoty zadośćuczynienia przez sąd II instancji względem wyroku I instancji; 'nie_dotyczy' dla orzeczeń sądu I instancji bez rozpatrywanej apelacji; pole kluczowe dla Q6",
            "name": "zmiana_kwoty_przez_sad_ii_instancji"
          },
          {
            "type_": "enum",
            "enum_name": "ZmianaOdszkodowaniaApelacja",
            "enum_values": [
              "podwyzszenie",
              "obnizenie",
              "brak_zmiany",
              "nie_dotyczy"
            ],
            "description": "Kierunek zmiany kwoty odszkodowania (art. 444 § 1 k.c.) przez sąd II instancji względem wyroku I instancji; 'nie_dotyczy' dla orzeczeń sądu I instancji lub gdy odszkodowanie nie było przedmiotem apelacji; pole kluczowe dla Q6",
            "name": "zmiana_odszkodowania_przez_sad_ii_instancji"
          },
          {
            "type_": "enum",
            "enum_name": "PowodyZmianyZadoscuczynieniaSadII",
            "enum_values": [
              "niedoszacowanie_krzywdy",
              "przeszacowanie_krzywdy",
              "korekta_metodologii_obliczenia",
              "nowe_okolicznosci_lub_dowody",
              "blad_procesowy_sad_i_instancji",
              "zmiana_zakresu_roszczenia",
              "inny",
              "nie_dotyczy"
            ],
            "description": "Główny powód zmiany kwoty zadośćuczynienia przez sąd II instancji wskazany w uzasadnieniu; 'korekta_metodologii_obliczenia' = zmiana wynikająca z innej logiki obliczenia lub zaliczenia świadczeń, nie z odmiennej oceny rozmiaru krzywdy; 'nie_dotyczy' jeśli sąd II instancji nie zmienił kwoty zadośćuczynienia lub orzeczenie pochodzi z I instancji; pole kluczowe dla Q6",
            "name": "powody_zmiany_zadoscuczynienia_sad_ii"
          },
          {
            "type_": "enum",
            "enum_name": "PowodyZmianyOdszkodowaniaSadII",
            "enum_values": [
              "blad_w_ustaleniu_szkody_majatkowej",
              "zmiana_zakresu_kosztow_uznanych",
              "korekta_metodologii_obliczenia",
              "nowe_dowody_kosztow",
              "blad_procesowy_sad_i_instancji",
              "zmiana_zakresu_roszczenia",
              "inny",
              "nie_dotyczy"
            ],
            "description": "Główny powód zmiany kwoty odszkodowania (art. 444 § 1 k.c.) przez sąd II instancji wskazany w uzasadnieniu; 'nie_dotyczy' jeśli sąd II instancji nie zmienił kwoty odszkodowania lub orzeczenie pochodzi z I instancji; pole kluczowe dla Q6",
            "name": "powody_zmiany_odszkodowania_sad_ii"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd uzasadnił odszkodowanie odrębnie od zadośćuczynienia, przedstawiając osobną argumentację co do szkody majątkowej; pole kluczowe dla Q9",
            "name": "odszkodowanie_uzasadnione_odrebnie"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wśród zasądzonych składników odszkodowania sąd uwzględnił koszty leczenia; pole kluczowe dla Q9",
            "name": "odszkodowanie_koszty_leczenia"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wśród zasądzonych składników odszkodowania sąd uwzględnił koszty rehabilitacji; pole kluczowe dla Q9",
            "name": "odszkodowanie_koszty_rehabilitacji"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wśród zasądzonych składników odszkodowania sąd uwzględnił utracony zarobek lub utratę zdolności zarobkowej; pole kluczowe dla Q9",
            "name": "odszkodowanie_utracony_zarobek"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wśród zasądzonych składników odszkodowania sąd uwzględnił inne koszty (np. opieki osób trzecich, dostosowania mieszkania, sprzętu pomocniczego); pole kluczowe dla Q9",
            "name": "odszkodowanie_inne_koszty"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wskazał zaniedbania o charakterze organizacyjnym podmiotu leczniczego (np. braki w procedurach, organizacji oddziału, dokumentacji) jako okoliczność wpływającą na wysokość zasądzonej kwoty — nie jako podstawę prawną odpowiedzialności, lecz jako czynnik miarkowania; pole kluczowe dla Q5",
            "name": "sad_wskazal_zaniedbania_organizacyjne_jako_okolicznosc_miarkowania"
          }
        ]
        ```

=== "Gemma 4 E4B IT"

    **23 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `instancja_sadowa` | string | Court instance issuing the ruling (first instance or appeal). |
        | `charakter_roszczenia_klasyfikacja` | enum | Main nature of the claim examined in the ruling, to which the awarded amounts relate. |
        | `typ_sprawy_podstawy_odpowiedzialnosci` | enum | Precise legal basis of liability (e.g. tort liability vs. medical-entity organizational liability, including informational liability). |
        | `typ_bledu_medycznego` | enum | Categorization of the type of medical error that caused the harm. |
        | `status_pozwanego` | enum | Legal status of the defendant (physician, medical entity, insurer). |
        | `charakter_szkody_fizycznej` | enum | Categorization of the nature of the patient's permanent health impairment. |
        | `analiza_opinii_biegla` | enum | Granular assessment of how the court used the expert's findings. |
        | `zgodnosc_biegly_vs_kwota` | enum | Assessment of the correlation between the expert's percentage impairment and the awarded amount. |
        | `wiek_pacjenta` | integer | Patient's age at the time of the event or the ruling, key for damage assessment. |
        | `procent_uszczerbku_glowny` | float | Main percentage of permanent health impairment, if stated by the expert and accepted by the court. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `instancja_sadowa` | string | Instancja sądowa wydająca orzeczenie (I instancji lub apelacyjna). |
        | `charakter_roszczenia_klasyfikacja` | enum | Główny charakter roszczenia badanego w orzeczeniu, do którego odnoszą się zasądzane kwoty. |
        | `typ_sprawy_podstawy_odpowiedzialnosci` | enum | Precyzyjna podstawa prawna odpowiedzialności, kluczowa dla kontekstu (np. deliktowa vs. odpowiedzialność podmiotu leczniczego, w tym informacyjna). |
        | `typ_bledu_medycznego` | enum | Kategoryzacja samego typu błędu medycznego, który doprowadził do szkody (kluczowa dla Q10). |
        | `status_pozwanego` | enum | Status prawny podmiotu pozwanego (lekarz, szpital/podmiot, ubezpieczyciel), kluczowa zmienna porównawcza. |
        | `charakter_szkody_fizycznej` | enum | Kategoryzacja charakteru trwałego uszczerbku na zdrowiu pacjenta (skutek). |
        | `analiza_opinii_biegla` | enum | Granularna ocena, jak sąd wykorzystał ustalenia biegłych (Q2). |
        | `zgodnosc_biegly_vs_kwota` | enum | Ocena korelacji między procentowym uszczerbkiem (z opinii) a kwotą zasądzoną (Q2). |
        | `wiek_pacjenta` | integer | Wiek pacjenta w chwili wystąpienia zdarzenia lub orzekania, kluczowy dla miarkowania. |
        | `procent_uszczerbku_glowny` | float | Główny procentowy stopień trwałego uszczerbku na zdrowiu, jeśli podany przez biegłego i przyjęty przez sąd. |
    ??? note "Show full schema (23 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "string",
            "enum_name": "instancja_sadowa",
            "enum_values": [
              "pierwsza_instancja",
              "apelacja"
            ],
            "description": "Instancja sądowa wydająca orzeczenie (I instancji lub apelacyjna).",
            "name": "instancja_sadowa"
          },
          {
            "type_": "enum",
            "enum_name": "charakter_roszczenia_klasyfikacja",
            "enum_values": [
              "zadośćuczynienie_krzywda",
              "odszkodowanie_majatek",
              "obydwa"
            ],
            "description": "Główny charakter roszczenia badanego w orzeczeniu, do którego odnoszą się zasądzane kwoty.",
            "name": "charakter_roszczenia_klasyfikacja"
          },
          {
            "type_": "enum",
            "enum_name": "typ_sprawy_podstawy_odpowiedzialnosci",
            "enum_values": [
              "odp_deliktowa_art_415_kc",
              "odp_organizacyjna_podmiot_leczniczy",
              "odp_informatywna",
              "inne_podstawy"
            ],
            "description": "Precyzyjna podstawa prawna odpowiedzialności, kluczowa dla kontekstu (np. deliktowa vs. odpowiedzialność podmiotu leczniczego, w tym informacyjna).",
            "name": "typ_sprawy_podstawy_odpowiedzialnosci"
          },
          {
            "type_": "enum",
            "enum_name": "typ_bledu_medycznego",
            "enum_values": [
              "diagnostyczny",
              "terapeutyczny",
              "informacyjny",
              "operacyjny",
              "inny"
            ],
            "description": "Kategoryzacja samego typu błędu medycznego, który doprowadził do szkody (kluczowa dla Q10).",
            "name": "typ_bledu_medycznego"
          },
          {
            "type_": "enum",
            "enum_name": "status_pozwanego",
            "enum_values": [
              "lekarz_osoba_fizyczna",
              "podmiot_leczniczy",
              "ubezpieczyciel"
            ],
            "description": "Status prawny podmiotu pozwanego (lekarz, szpital/podmiot, ubezpieczyciel), kluczowa zmienna porównawcza.",
            "name": "status_pozwanego"
          },
          {
            "type_": "enum",
            "enum_name": "charakter_szkody_fizycznej",
            "enum_values": [
              "ograniczenie_funkcjonalne",
              "utrata_narządu_części_ciała",
              "choroba_przewlekła",
              "uszkodzenie_neuronalne",
              "brak_trwałego_uszkodzenia",
              "inny"
            ],
            "description": "Kategoryzacja charakteru trwałego uszczerbku na zdrowiu pacjenta (skutek).",
            "name": "charakter_szkody_fizycznej"
          },
          {
            "type_": "enum",
            "enum_name": "analiza_opinii_biegla",
            "enum_values": [
              "bazuje_wprost_na_opinii",
              "wykracza_poza_opinii_interpretacja_sadu",
              "wykracza_poza_opinii_odchylenie_faktyczne",
              "opinia_nie_była_kluczowa_dla_wyroku"
            ],
            "description": "Granularna ocena, jak sąd wykorzystał ustalenia biegłych (Q2).",
            "name": "analiza_opinii_biegla"
          },
          {
            "type_": "enum",
            "enum_name": "zgodnosc_biegly_vs_kwota",
            "enum_values": [
              "zgodna_procentowo",
              "wykracza_poza_biegla_podwyzszenie",
              "wykracza_poza_biegla_obniszenie",
              "nie_określona"
            ],
            "description": "Ocena korelacji między procentowym uszczerbkiem (z opinii) a kwotą zasądzoną (Q2).",
            "name": "zgodnosc_biegly_vs_kwota"
          },
          {
            "type_": "integer",
            "enum_name": "wiek_pacjenta_lat",
            "enum_values": [],
            "description": "Wiek pacjenta w chwili wystąpienia zdarzenia lub orzekania, kluczowy dla miarkowania.",
            "name": "wiek_pacjenta"
          },
          {
            "type_": "float",
            "enum_name": "procent_uszczerbku_glowny",
            "enum_values": [],
            "description": "Główny procentowy stopień trwałego uszczerbku na zdrowiu, jeśli podany przez biegłego i przyjęty przez sąd.",
            "name": "procent_uszczerbku_glowny"
          },
          {
            "type_": "string",
            "enum_name": "inne_skomponenty_procentowe",
            "enum_values": [],
            "description": "Lista dodatkowych, mniejszych procentowych składowych uszczerbku, jeśli są wyodrębnione przez sąd/biegłego.",
            "name": "inne_skomponenty_procentowe"
          },
          {
            "type_": "boolean",
            "enum_name": "odwolanie_do_porownan",
            "enum_values": [],
            "description": "Czy sąd w uzasadnieniu bezpośrednio odwołuje się do porównań z innymi podobnymi orzeczeniami (Q4).",
            "name": "odwolanie_do_porownan"
          },
          {
            "type_": "enum",
            "enum_name": "uzasadnienie_kwoty_kryteria",
            "enum_values": [
              "porownanie_z_orzecznictwem",
              "analiza_faktyczna_szkody",
              "funkcja_kompensacyjna",
              "inne_uwarunkowania_społeczne"
            ],
            "description": "Główne kryterium, na którym sąd oprzeł uzasadnienie wysokości świadczenia (Q4).",
            "name": "uzasadnienie_kwoty_kryteria"
          },
          {
            "type_": "string",
            "enum_name": "opis_cierpienia_fizyczno_psychicznego",
            "enum_values": [],
            "description": "Podsumowanie oceny przez sąd intensywności i czasu trwania cierpienia fizycznego i psychicznego (aspekt subiektywny, kluczowy dla zadośćuczynienia).",
            "name": "opis_cierpienia_fizyczno_psychicznego"
          },
          {
            "type_": "string",
            "enum_name": "opis_wplywu_zawodowego",
            "enum_values": [],
            "description": "Szczegółowy opis stopnia wpływu uszczerbku na zdolność pacjenta do wykonywania pracy (kluczowy dla odszkodowania).",
            "name": "opis_wplywu_zawodowego"
          },
          {
            "type_": "string",
            "enum_name": "opis_skutkow_inne",
            "enum_values": [],
            "description": "Szczegółowy opis innych istotnych skutków społecznych, psychicznych lub domowych uwzględnionych w uzasadnieniu (np. utrata samodzielności, wpływ na rodzinę, Q7).",
            "name": "opis_skutkow_inne"
          },
          {
            "type_": "string",
            "enum_name": "specyficzne_koszty_leczenia_PLN",
            "enum_values": [],
            "description": "Szczegółowy wykaz zasądzonych kosztów leczenia, rehabilitacji i opieki po zdarzeniu (składnik odszkodowania).",
            "name": "specyficzne_koszty_leczenia_PLN"
          },
          {
            "type_": "string",
            "enum_name": "utracony_dochod_PLN",
            "enum_values": [],
            "description": "Szczegółowy wykaz zasądzonych dochodów, które pacjent utracił lub utracił przewidywany (składnik odszkodowania).",
            "name": "utracony_dochod_PLN"
          },
          {
            "type_": "enum",
            "enum_name": "kierunek_zmiany_kwoty_apelacja",
            "enum_values": [
              "zmniejszono",
              "zwiększono",
              "bez_zmiany",
              "nie_dotyczy"
            ],
            "description": "Kierunek zmiany kwoty świadczenia przez sąd odwoławczy w stosunku do sądu I instancji (Q5).",
            "name": "kierunek_zmiany_kwoty_apelacja"
          },
          {
            "type_": "string",
            "enum_name": "konkretne_fakty_sprawy",
            "enum_values": [],
            "description": "Katalog obiektywnych faktów charakteryzujących sprawę, niezwiązanych bezpośrednio z subiektywnym cierpieniem (np. 'Uszkodzenie nerwu X', 'Błąd w procedurze Y').",
            "name": "konkretne_fakty_sprawy"
          },
          {
            "type_": "string",
            "enum_name": "kwoty_zasadzone",
            "enum_values": [],
            "description": "Lista szczegółowych zasądzonych kwot. Każdy element listy powinien być obiektem zawierającym kwotę ('value') i jej typ ('type': 'zadośćuczynienie' lub 'odszkodowanie').",
            "name": "kwoty_zasadzone"
          },
          {
            "type_": "float",
            "enum_name": "total_zadośćuczynienie_pln",
            "enum_values": [],
            "description": "Suma wszystkich kwot zasądzonych tytułem zadośćuczynienia w tym orzeczeniu.",
            "name": "total_zadośćuczynienie_pln"
          },
          {
            "type_": "float",
            "enum_name": "total_odszkodowanie_pln",
            "enum_values": [],
            "description": "Suma wszystkich kwot zasądzonych tytułem odszkodowania w tym orzeczeniu.",
            "name": "total_odszkodowanie_pln"
          }
        ]
        ```

=== "GPT-5.4 nano"

    **48 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `claim_type_primary` | enum | Dominant type of monetary claim analyzed — compensation, damages, both, or other. |
        | `liability_source` | enum | Nature/source of liability described in the reasoning or facts — medical error, workplace accident, other tort. |
        | `defendant_status_primary` | enum | Dominant status of the defendant — medical entity/hospital, insurer, physician as a natural person, State Treasury/public entity, etc. |
        | `pct_uszczerbek_source_type` | enum | Source of the percentage/numeric parameter used to determine the extent of permanent health impairment. |
        | `expert_opinion_used` | boolean | Whether a credible expert/medical opinion was used to determine the extent of the harm. |
        | `expert_provided_pct_uszczerbek` | boolean | Whether a percentage figure appears in the ruling in the context of permanent health impairment. |
        | `expert_pct_uszczerbek_source_explicit` | boolean | Whether the court explicitly states that the percentage/numeric parameter comes from an expert opinion or other medical document. |
        | `expert_pct_uszczerbek_value_present` | boolean | Whether the reasoning explicitly states a specific percentage value for the permanent impairment. |
        | `expert_pct_uszczerbek_value` | float | Value of the percentage impairment (in %), if stated explicitly. |
        | `court_explicitly_connected_pct_to_amount` | boolean | Whether the reasoning explicitly ties the awarded amount to a percentage impairment value. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `claim_type_primary` | enum | Dominujący typ świadczenia/roszczenia pieniężnego, którego wysokość ma być analizowana (rdzeń ilościowy). Wypełniaj na podstawie sentencji/rozstrzygnięcia. Jeśli w tej samej sprawie występują równolegle zarówno zadośćuczynienie, jak i odszkodowanie, wybierz `oba_zadośćuczynienie_i_odszkodowanie` (żeby ograniczyć arbitralność). |
        | `liability_source` | enum | Charakter/źródło odpowiedzialności opisane w uzasadnieniu lub w podstawie faktycznej. Jeśli zdarzenie nie jest „medycznym błędem” (np. wypadek przy pracy), ustaw wartość inną niż `błąd_medyczny`. |
        | `defendant_status_primary` | enum | Dominujący status pozwanego (lub strony dominującej w odpowiedzialności). Dobieraj kategorię wg tego, kto jest wskazywany jako podmiot odpowiedzialny (zwykle wątek odpowiedzialności organizacyjnej/organizacyjno-instytucjonalnej, ubezpieczyciel/OC, itd.). W sprawach ze Skarbem Państwa wybieraj `skarb_panstwa_jednostka_publiczna` (np. dyrektor szpitala w strukturze publicznej/jednostka publiczna). Jeśli rozstrzygnięcie dotyczy konkretnie dyrektora jednostki penitencjarnej – wybierz `dyrektor_jednostki_penitencjarnej`. |
        | `pct_uszczerbek_source_type` | enum | Źródło parametru procentowego/liczbowego używanego do ustaleń o rozmiarze trwałych następstw (np. uszczerbek w %). Jeśli sąd operuje innym dokumentem medycznym/orzeczeniem poza ZUS – koduj jako `inne_orzeczenie_medyczne`. |
        | `expert_opinion_used` | boolean | Czy w sprawie wykorzystano wiarygodne źródło opiniodawcze/medyczne do ustaleń rozmiaru krzywdy/niepełnosprawności/uszczerbku (np. opinie biegłych sądowych i/lub orzeczenia ZUS)? |
        | `expert_provided_pct_uszczerbek` | boolean | Czy w treści orzeczenia/uzasadnienia pojawia się liczba w formie procentu w kontekście uszczerbku/trwałych następstw (niezależnie od tego, czy pochodzi z opinii biegłych czy z orzeczeń ZUS)? |
        | `expert_pct_uszczerbek_source_explicit` | boolean | Czy sąd wprost wskazuje, że podany procent/liczbowy parametr pochodzi z opinii biegłych lub innego dokumentu medycznego/ZUS (np. „biegli przyjęli 8%”, „z orzeczenia wynika 8%”)? |
        | `expert_pct_uszczerbek_value_present` | boolean | Czy uzasadnienie zawiera wprost konkretną wartość procentową (lub równoważny parametr liczbowy) w kontekście trwałych następstw? Uwaga: różne formy liczb (np. „8 procent”) też wliczają się do tej kategorii. |
        | `expert_pct_uszczerbek_value` | float | Wartość procentowego uszczerbku (w %), jeśli wskazana wprost (lub równoważny parametr liczbowy przeliczony do procentów na poziomie tekstu – gdy tekst nie rozróżnia jednostek, wpisz liczbę). |
        | `court_explicitly_connected_pct_to_amount` | boolean | Czy uzasadnienie miarkowania wprost łączy zastosowaną kwotę z wartością procentu/uszczerbku (np. „kwota odpowiada 8%” / „w oparciu o 8% zasądza…”)? Jeśli sąd wspomina procent, ale nie pokazuje mechanizmu „% → kwota”, koduj `false`. |
    ??? note "Show full schema (48 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "zadośćuczynienie",
              "odszkodowanie_szkoda_majątkowa",
              "zwrot_kosztów_opieki_zwiększonych_potrzeb",
              "odszkodowanie_za_utracone_dochody",
              "inna_forma_świadczenia",
              "oba_zadośćuczynienie_i_odszkodowanie",
              "brak_danych"
            ],
            "description": "Dominujący typ świadczenia/roszczenia pieniężnego, którego wysokość ma być analizowana (rdzeń ilościowy). Wypełniaj na podstawie sentencji/rozstrzygnięcia. Jeśli w tej samej sprawie występują równolegle zarówno zadośćuczynienie, jak i odszkodowanie, wybierz `oba_zadośćuczynienie_i_odszkodowanie` (żeby ograniczyć arbitralność).",
            "name": "claim_type_primary"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "błąd_medyczny",
              "wypadek_przy_pracy",
              "inne_zdarzenie_deliktowe",
              "brak_danych"
            ],
            "description": "Charakter/źródło odpowiedzialności opisane w uzasadnieniu lub w podstawie faktycznej. Jeśli zdarzenie nie jest „medycznym błędem” (np. wypadek przy pracy), ustaw wartość inną niż `błąd_medyczny`.",
            "name": "liability_source"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "podmiot_leczniczy_szpital",
              "ubezpieczyciel",
              "lekarz_osoba_fizyczna",
              "kilku_pozwanych_rożne_statusy",
              "pracodawca_inna_strona",
              "skarb_panstwa_jednostka_publiczna",
              "dyrektor_jednostki_penitencjarnej",
              "inne",
              "brak_danych"
            ],
            "description": "Dominujący status pozwanego (lub strony dominującej w odpowiedzialności). Dobieraj kategorię wg tego, kto jest wskazywany jako podmiot odpowiedzialny (zwykle wątek odpowiedzialności organizacyjnej/organizacyjno-instytucjonalnej, ubezpieczyciel/OC, itd.). W sprawach ze Skarbem Państwa wybieraj `skarb_panstwa_jednostka_publiczna` (np. dyrektor szpitala w strukturze publicznej/jednostka publiczna). Jeśli rozstrzygnięcie dotyczy konkretnie dyrektora jednostki penitencjarnej – wybierz `dyrektor_jednostki_penitencjarnej`.",
            "name": "defendant_status_primary"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "biegli_sądowi",
              "orzeczenie_lekarza_zus_orzecznik",
              "inne_orzeczenie_medyczne",
              "brak_danych"
            ],
            "description": "Źródło parametru procentowego/liczbowego używanego do ustaleń o rozmiarze trwałych następstw (np. uszczerbek w %). Jeśli sąd operuje innym dokumentem medycznym/orzeczeniem poza ZUS – koduj jako `inne_orzeczenie_medyczne`.",
            "name": "pct_uszczerbek_source_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w sprawie wykorzystano wiarygodne źródło opiniodawcze/medyczne do ustaleń rozmiaru krzywdy/niepełnosprawności/uszczerbku (np. opinie biegłych sądowych i/lub orzeczenia ZUS)?",
            "name": "expert_opinion_used"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w treści orzeczenia/uzasadnienia pojawia się liczba w formie procentu w kontekście uszczerbku/trwałych następstw (niezależnie od tego, czy pochodzi z opinii biegłych czy z orzeczeń ZUS)?",
            "name": "expert_provided_pct_uszczerbek"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wprost wskazuje, że podany procent/liczbowy parametr pochodzi z opinii biegłych lub innego dokumentu medycznego/ZUS (np. „biegli przyjęli 8%”, „z orzeczenia wynika 8%”)?",
            "name": "expert_pct_uszczerbek_source_explicit"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy uzasadnienie zawiera wprost konkretną wartość procentową (lub równoważny parametr liczbowy) w kontekście trwałych następstw? Uwaga: różne formy liczb (np. „8 procent”) też wliczają się do tej kategorii.",
            "name": "expert_pct_uszczerbek_value_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Wartość procentowego uszczerbku (w %), jeśli wskazana wprost (lub równoważny parametr liczbowy przeliczony do procentów na poziomie tekstu – gdy tekst nie rozróżnia jednostek, wpisz liczbę).",
            "name": "expert_pct_uszczerbek_value"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy uzasadnienie miarkowania wprost łączy zastosowaną kwotę z wartością procentu/uszczerbku (np. „kwota odpowiada 8%” / „w oparciu o 8% zasądza…”)? Jeśli sąd wspomina procent, ale nie pokazuje mechanizmu „% → kwota”, koduj `false`.",
            "name": "court_explicitly_connected_pct_to_amount"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "pct_uszczerbek_jako_główny_wyznacznik",
              "pozostale_mierniki_jako_główne",
              "mieszane_pct_i_opis_niemierzalny",
              "brak_ujawnionego_mechanizmu_przeliczenia_pct_na_kwote",
              "brak_jasności_lub_brak_danych",
              "nie_dotyczy"
            ],
            "description": "Ustal „centrum ciężkości” miarkowania: czy sąd traktuje procent/uszczerbek jako klucz do kwoty, czy głównie inne czynniki (opis cierpień, trwałość, rokowania). Wybieraj `brak_ujawnionego_mechanizmu_przeliczenia_pct_na_kwote`, gdy procent występuje, ale z tekstu nie da się rzetelnie ocenić, że był przeliczony na kwotę.",
            "name": "court_primary_amount_driver"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "zgodne_w_przeważającej_części_z_pct",
              "korygowano_względem_pct_w_górę",
              "korygowano_względem_pct_w_dół",
              "sąd_uwzględnił_pct_ale_nie_stosował_jako_miernika_kwoty",
              "brak_materialnej_podstawy_do_oceny_relacji_pct_i_kwoty",
              "brak_pct_w_opiniach_uwypuklonych_lub_w_uzasadnieniu",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Relacja między ostateczną ujętą kwotą a procentem/uszczerbkiem wynikającym z tekstu. Koduj tylko na podstawie tego, co da się uzasadnić z fragmentów porównawczych. Jeśli w tekście nie ma porównania/wyliczenia, wybierz `brak_materialnej_podstawy_do_oceny_relacji_pct_i_kwoty` zamiast zgadywać korektę.",
            "name": "court_alignment_with_expert_pct"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "korekta_powodowana_trwałością_i_nieodwracalnością",
              "korekta_powodowana_intensywnością_cierpień",
              "korekta_powodowana_istotnym_oddziaływaniem_na_życie_zawodowe_rodzinne",
              "korekta_powodowana_rozbieżnością_z_dokumentacją_med",
              "korekta_powodowana_wnioskami_o_rokowaniach_lub_przebiegu",
              "korekta_nieopisana_wprost",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Główna kategoria powodu odejścia od % lub sposobu wykorzystania % przy miarkowaniu. Gate: wypełniaj sensownie tylko wtedy, gdy `court_explicitly_connected_pct_to_amount=true` i w tekście jest mowa o korekcie/odstępstwie; w przeciwnym razie ustaw `nie_dotyczy` lub `brak_danych` (gdy nie da się ustalić z tekstu, czy korekta wystąpiła).",
            "name": "departure_reason_category"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "błąd_diagnostyczny",
              "błąd_terapeutyczny",
              "błąd_okołoporodowy",
              "inne",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Kontekst medyczny błędu, wyłącznie gdy `liability_source=błąd_medyczny`. Jeśli zdarzenie nie jest błędem medycznym, koduj `nie_dotyczy`. Gdy w tekście współwystępuje kilka kontekstów, wybierz ten dominujący dla ustaleń sądu.",
            "name": "medical_error_context_type"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "brak_procedury_zaniedbanie_kontroli",
              "błąd_organizacyjny_lub_wina_organizacyjna_konieczne_zasobowe",
              "inne",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Wymiar proceduralno-organizacyjny/wina organizacyjna (jeśli występuje) — wyłącznie gdy `liability_source=błąd_medyczny`. Jeśli sąd nie opisuje takiego wymiaru, koduj `brak_danych` albo `nie_dotyczy` (w zależności od tego, czy w ogóle odpowiedzialność wynika z błędu medycznego).",
            "name": "medical_error_procedural_fault_type"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "psychiczna",
              "fizyczna",
              "mieszana",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Dominujący charakter krzywdy akcentowany w uzasadnieniu miarkowania zadośćuczynienia. `psychiczna`: stres/cierpienia psychiczne/uraz psychiczny; `fizyczna`: ból cierpienia somatyczne; `mieszana`: istotnie oba. Jeśli brak zadośćuczynienia, koduj `nie_dotyczy`.",
            "name": "dominant_krzywda_category"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd ograniczył zakres odpowiedzialności / odciął część skutków (np. uznał, że nie wszystko wynika z błędu, albo że część następstw nie podlega odpowiedzialności)?",
            "name": "liability_scope_cut_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "ograniczono_do_części_skutków",
              "uznano_część_skutków_za_brak_odpowiedzialności",
              "ograniczono_odpowiedzialność_z_innych_powodów",
              "inne",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Jeśli `liability_scope_cut_present=true`: jaki był dominujący typ „odcięcia”/ograniczenia opisany w uzasadnieniu. Jeśli nie występuje, ustaw `nie_dotyczy`.",
            "name": "liability_scope_cut_description"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd wskazuje przyczynienie pacjenta lub inne okoliczności po stronie pacjenta, które wpływają na aktualny stan (np. brak współpracy, nieprzestrzeganie zaleceń, podjęcie nieadekwatnej terapii)?",
            "name": "plaintiff_contribution_to_current_state_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "brak_współpracy/nieprzestrzeganie_zaleceń",
              "podjęcie_nieadekwatnej_terapii",
              "nawyki_ryzykowne",
              "inne",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Jeśli `plaintiff_contribution_to_current_state_present=true`: kategoria dominująca dla okoliczności przypisanych pacjentowi. Jeśli nie ma tej podstawy, ustaw `nie_dotyczy`.",
            "name": "plaintiff_contribution_category"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd rozstrzygnął roszczenie o zadośćuczynienie (w całości lub części)? Gate: jeśli `has_zadosc=false`, pola ilościowe dot. zadośćuczynienia powinny być `nie_dotyczy`/pominięte lub zakodowane jako brak danych zgodnie z konwencją.",
            "name": "has_zadosc"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "kwota_glówna_bez_odsetek",
              "kwota_z_odsetkami_lub_w_części_z_odsetkami",
              "nieokreślone_czy_obejmuje_odsetki",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Definicja, czy kwota zadośćuczynienia w danych dotyczy kwoty głównej (bez odsetek) czy jest podana wraz z odsetkami/częściowo z odsetkami. Odczytuj wg sentencji (np. czy sąd rozdziela: „kwota z odsetkami od dnia…”).",
            "name": "zado_s_amount_definition"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy żądana kwota zadośćuczynienia jest podana w materiale (w pozwie/żądaniu/ustaleniach)? Gate: przy braku zadośćuczynienia ustaw `nie_dotyczy`.",
            "name": "claimed_zadosc_pln_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Żądana kwota zadośćuczynienia (PLN) jeśli podana w rozstrzygnięciu/żądaniu.",
            "name": "claimed_zadosc_pln"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy zasądzona kwota zadośćuczynienia jest podana. UWAGA spójność: jeśli `has_zadosc=true` i `zadosc_disposition_category` wskazuje oddalenie w całości/części, ustaw domyślnie `awarded_zadosc_zero_amount=true`, `awarded_zadosc_pln=0` oraz `awarded_zadosc_pln_present=true` (jeżeli w sentencji nie ma wprost „0 zł”, kodowanie wykonaj na podstawie wyniku: brak uwzględnienia).",
            "name": "awarded_zadosc_pln_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Łączna kwota zasądzona z tytułu zadośćuczynienia (pacjent i/lub osoby bliskie), w PLN.",
            "name": "awarded_zadosc_pln"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy odsetki od zadośćuczynienia są przedmiotem rozstrzygnięcia?",
            "name": "interest_on_zadosc_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "od_dnia_wyrokowania",
              "od_dnia_złożenia_pozwu_wezwania",
              "od_dnia_zdarzenia",
              "od_dnia_innego_określonego_w_uzasadnieniu",
              "nie_dotyczy",
              "brak_danych"
            ],
            "description": "Moment początkowy naliczania odsetek od zadośćuczynienia wg sentencji/uzasadnienia.",
            "name": "interest_zadosc_period_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd odwoławczy zmienił kwotę zadośćuczynienia względem instancji niższej (dla porównywalnego zakresu)? Gate: jeśli brak weryfikacji odwoławczej lub brak zadośćuczynienia — nie wypełniaj/zakoduj jako brak danych zgodnie z konwencją.",
            "name": "has_appellate_review"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "oddalono_w_całości",
              "oddalono_częściowo",
              "zasądzono_częściowo",
              "zasądzono_w_całości",
              "umorzono",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Dyspozycja w przedmiocie roszczenia o zadośćuczynienie.",
            "name": "zadosc_disposition_category"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd rozstrzygnął, że zadośćuczynienie nie przysługuje (wartość uwzględniona = 0). Gate: wypełniaj logicznie spójnie z `zadosc_disposition_category` i opisem dla `awarded_zadosc_pln_present`.",
            "name": "awarded_zadosc_zero_amount"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "podwyższono",
              "obniżono",
              "utrzymano",
              "brak_materialnych_porównań_w_dokumencie",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Jeśli `has_appellate_review=true`: kierunek zmiany kwoty zadośćuczynienia w II instancji względem I instancji (podwyższono/obniżono/utrzymano). Gdy dokument nie zawiera porównania kwot lub nie da się ustalić kierunku, koduj `brak_materialnych_porównań_w_dokumencie`. Jeśli brak odwoławczego rozstrzygnięcia – `nie_dotyczy`.",
            "name": "appellate_review_zadosc_change_direction"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd rozstrzygnął roszczenie o odszkodowanie (szkoda majątkowa)? Gate: jeśli `has_odszkodowanie=false`, pola ilościowe i odsetkowe dot. odszkodowania koduj jako `nie_dotyczy` zgodnie z konwencją.",
            "name": "has_odszkodowanie"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy żądana kwota odszkodowania jest podana w materiale (w pozwie/żądaniu/ustaleniach)? Gate: przy braku odszkodowania ustaw `nie_dotyczy`.",
            "name": "claimed_odszkodowanie_pln_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Żądana kwota odszkodowania (PLN), jeśli wskazana w materiale lub w ustaleniach sądu.",
            "name": "claimed_odszkodowanie_pln"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd zasądził/uwzględnił odszkodowanie oraz czy kwota jest podana (albo wynika z braku uwzględnienia)? Gate: jeśli `has_odszkodowanie=false` -> `nie_dotyczy`/pomijaj.",
            "name": "awarded_odszkodowanie_pln_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Łączna kwota zasądzona tytułem odszkodowania (szkoda majątkowa), w PLN. Jeśli roszczenie oddalono w całości i dokument pozwala to zakodować jako 0, wpisz 0.",
            "name": "awarded_odszkodowanie_pln"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd rozstrzygnął, że odszkodowanie nie przysługuje (wartość uwzględniona = 0). Używaj jako analogii do `awarded_zadosc_zero_amount` dla zadośćuczynienia.",
            "name": "awarded_odszkodowanie_zero_amount"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy odsetki od odszkodowania są przedmiotem rozstrzygnięcia?",
            "name": "interest_on_odszkodowanie_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "od_dnia_wyrokowania",
              "od_dnia_złożenia_pozwu_wezwania",
              "od_dnia_zdarzenia",
              "od_dnia_innego_określonego_w_uzasadnieniu",
              "nie_dotyczy",
              "brak_danych"
            ],
            "description": "Moment początkowy naliczania odsetek od odszkodowania wg sentencji/uzasadnienia.",
            "name": "interest_odszkodowanie_period_type"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "podwyższono",
              "obniżono",
              "utrzymano",
              "brak_materialnych_porównań_w_dokumencie",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "Jeśli istnieje kontrola instancyjna odwoławcza obejmująca odszkodowanie: kierunek zmiany kwoty odszkodowania w II instancji względem I instancji. Jeśli nie da się ustalić kierunku z treści – `brak_materialnych_porównań_w_dokumencie`. Jeśli brak takiej weryfikacji – `nie_dotyczy`.",
            "name": "appellate_review_odszkodowanie_change_direction"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd zasądził/uwzględnił zwrot kosztów opieki / wydatków zwiększonych potrzeb (jeżeli występuje w danej sprawie)?",
            "name": "awarded_costs_opieki_pln_present"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota zasądzona tytułem zwrotu kosztów opieki (jeżeli podana wprost jako łączna kwota), w PLN.",
            "name": "awarded_costs_opieki_pln"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Rok początkowy okresu, za który zasądzono zwrot kosztów opieki (jeśli opisany). Wpisuj tylko rok liczbowy (np. 2019).",
            "name": "costs_opieki_period_start_year"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Rok końcowy okresu, za który zasądzono zwrot kosztów opieki (jeśli opisany). Wpisuj tylko rok liczbowy (np. 2020).",
            "name": "costs_opieki_period_end_year"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd uznał związek przyczynowy między wskazywanym błędem medycznym a szkodą (krzywdą/ następstwami)? Wypełniaj na podstawie fragmentów uzasadnienia dot. causality (np. „związek przyczynowy został wykazany/nie wykazano”).",
            "name": "causation_established"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "tak",
              "nie",
              "nie_dotyczy"
            ],
            "description": "Czy sąd uznał podstawę przypisania odpowiedzialności (wina/zawinienie w rozumieniu uzasadnienia albo inne kwalifikowane zawinienie, jeśli sąd to wprost wskazuje). W razie braku konieczności badania zawinienia (np. schemat odpowiedzialności o innym charakterze w danym stanie faktycznym – jeśli sąd tego nie analizuje wprost), koduj `nie_dotyczy`. Jeśli sąd stwierdził brak tej przesłanki – koduj `nie`.",
            "name": "fault_or_incrimination_established"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "tak",
              "nie",
              "brak_danych",
              "nie_dotyczy"
            ],
            "description": "W sprawach typowo „opóźnionej diagnostyki/rokowania”: czy sąd wprost rozważył wariant kontrfaktyczny, że nawet wcześniejsza diagnoza/leczenie nie zmieniłoby przebiegu lub rokowań? `tak` – gdy sąd tak stwierdza; `nie` – gdy sąd uznaje, że wcześniejsze działania mogły zmienić; `nie_dotyczy` – gdy nie ma wątku kontrfaktycznego; `brak_danych` – gdy brak wyraźnej oceny w tekście.",
            "name": "even_if_earlier_diagnosis_changed_nothing"
          }
        ]
        ```

