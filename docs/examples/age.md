# Age at Sentencing

The relationship between a defendant's age and sentence severity in drug-offense cases.

!!! info "About the English text on this page"
    This run was performed in Polish — the prompts, conversation, and generated schema field
    descriptions are all originally in Polish. The English tabs are machine translations
    produced after the fact for readability.

## The conversation

=== "🇬🇧 English"

    <div class="chat" markdown="1">
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">You</span>

    Generate a schema for extracting data from court rulings on drug-related crimes, with particular focus on the defendant's age and the severity of the sentence handed down.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Assistant</span>

    1. [Confirmation] Do I understand correctly that you want to study the relationship between the defendant's age and the severity of the sentence in drug-crime cases, based on the reasoning sections of Polish court judgments?

    2. [Legal framework] Are you interested in specific offense types under the Act of 29 July 2005 on Counteracting Drug Addiction (e.g. Art. 62, 59, 56, 58), and do you want to compare how the legal classification affects the sentence?

    3. [Legal framework] Do you also want to analyze relevant provisions of the Penal Code and the Executive Penal Code relevant to sentencing (e.g. Art. 53, 60, 69-72 KK) as potential factors differentiating sentence severity?

    4. [Procedural context] Are you limiting the study to convictions, or also including acquittals, discontinuations (including conditional discontinuation), and combined sentences where they occur in drug cases?

    5. [Procedural context] Is it important to distinguish between a juvenile defendant, a "young adult" under Art. 115 §10 KK, and an "adult" defendant as separate comparison categories?

    6. [Case-law analysis] Are you interested in whether courts differentiate sentence severity depending on typical mitigating/aggravating circumstances (e.g. prior convictions, addiction, financial motive, complicity, recidivism)?

    7. [Case-law analysis] Do you want to study the effect of the amount and type of drug/psychotropic substance and the purpose of possession (own use vs. dealing) on sentence severity — independent of the defendant's age?

    8. [Temporal context] Are you interested in whether the case law on sentencing for drug offenses has changed over time, and should "time of offense" be an analytical variable?

    9. [Special cases] Do you want to separate out cases involving defendants near the age of majority (e.g. 17-19), school/academic-context cases, or cases with parallel offenses, to check whether these contexts modify sentence severity?

    </div>
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">You</span>

    1. Yes.
    2. All drug offenses — possession, dealing, production.
    3. Yes, especially provisions on suspended sentences and conditional discontinuation.
    4. Convictions and conditional discontinuations. No acquittals.
    5. Yes, that's an important variable — I want those categories. I'd also like to split the defendant's age into 5 age brackets.
    6. Yes, all of those circumstances matter.
    7. Yes, the amount and type of substance matter. So does the purpose.
    8. No, I'm not interested in how case law changed over time.
    9. No, I don't want to separate that out, since it would already be captured by the defendant's age. I would like to analyze parallel offenses too, since they may affect the sentence.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Assistant</span>

    We're studying whether and how the defendant's age affects the type and severity of the criminal response in drug-offense cases, covering convictions and conditional discontinuations (no acquittals), and distinguishing juvenile, young-adult, and adult defendants as well as five age brackets. We also account for the amount and type of substance, the purpose of the act, suspended sentences, and mitigating/aggravating circumstances (prior convictions, recidivism, complicity, financial motive). The legal basis is the Drug Act and the Penal Code; changes in case law over time are out of scope.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Assistant</span>

    Based on your request, I've prepared an extraction schema for analyzing Polish court rulings in drug-offense cases, focusing on how the defendant's age affects the type and severity of the criminal response. It covers convictions and conditional discontinuations, no acquittals, and distinguishes juvenile, young-adult, and adult defendants, plus a 5-bracket age split.

    The current schema covers three main areas: document and case data, defendant data, and offense and sentence data. It extracts, among other things, the document type, its role and source in the ruling, the offense's legal classification, the type of drug offense, substance amount and category, the purpose of the act, the defendant's age at the time of the offense and at sentencing, plus the sentence type, its severity, suspension, conditional discontinuation, probation period, legal basis, and mitigating/aggravating circumstances. It also captures prior convictions, recidivism, addiction, financial motive, complicity, and parallel offenses.

    The schema is thus tailored to analyzing whether and how age and case context relate to sentence severity in drug cases. If you'd like, you can now point out anything to refine, simplify, or add.

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

    Wygeneruj schemat do ekstrakcji danych z orzeczeń sądowych dotyczących przestępstw narkotykowych, ze szczególnym uwzględnieniem wieku oskarżonego oraz wysokości orzeczonej kary.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Asystent</span>

    1. [Potwierdzenie] Czy dobrze rozumiem, że chcesz zbadać zależność między wiekiem oskarżonego a wysokością orzeczonej kary w sprawach dotyczących przestępstw narkotykowych, na podstawie uzasadnień polskich wyroków sądowych?

    2. [Ramy prawne] Czy interesują Cię konkretne typy czynów z ustawy z dnia 29 lipca 2005 r. o przeciwdziałaniu narkomanii (np. art. 62, art. 59, art. 56, art. 58), i czy chcesz porównać, jak kwalifikacja prawna wpływa na wymiar kary?

    3. [Ramy prawne] Czy chcesz analizować także przepisy Kodeksu karnego i Kodeksu karnego wykonawczego istotne dla wymiaru kary (np. art. 53 k.k., art. 60 k.k., art. 69–72 k.k.), jako potencjalne czynniki różnicujące surowość kary?

    4. [Kontekst procesowy] Czy ograniczasz badanie do wyroków skazujących, czy uwzględniasz również uniewinnienia, umorzenia (w tym warunkowe umorzenie postępowania) oraz wyroki łączne, jeśli pojawiają się w sprawach narkotykowych?

    5. [Kontekst procesowy] Czy istotne jest dla Ciebie rozróżnienie między oskarżonym nieletnim (postępowanie w sprawach nieletnich) a młodocianym w rozumieniu art. 115 § 10 k.k. oraz „dorosłym” oskarżonym — jako odrębne kategorie porównawcze?

    6. [Analiza orzecznictwa] Czy interesuje Cię, czy sądy w uzasadnieniach różnicują wymiar kary w zależności od okoliczności łagodzących/obciążających typowych dla tych spraw (np. uprzednia karalność, uzależnienie, działanie w celu osiągnięcia korzyści majątkowej, współsprawstwo, recydywa)?

    7. [Analiza orzecznictwa] Czy chcesz badać wpływ „ilości i rodzaju środka odurzającego/substancji psychotropowej” oraz celu posiadania (na własny użytek vs. obrót) na wysokość kary — niezależnie od wieku oskarżonego?

    8. [Kontekst temporalny] Czy interesuje Cię, czy linia orzecznicza w zakresie wymiaru kary za przestępstwa narkotykowe zmieniała się w czasie (np. po nowelizacjach Kodeksu karnego lub ustawy o przeciwdziałaniu narkomanii), i czy „moment czynu” ma być zmienną analityczną?

    9. [Przypadki szczególne] Czy chcesz wyodrębnić jako osobne scenariusze sprawy z udziałem osób w wieku bliskim granicy pełnoletności (np. 17–19 lat), sprawy szkolne/akademickie, albo sprawy z równoległymi czynami (np. art. 178a k.k., art. 157 k.k.), aby sprawdzić, czy te konteksty modyfikują surowość kary?


    </div>
    <div class="chat-msg chat-user" markdown="1">
    <span class="chat-label">Ty</span>

    1. Tak.
    2. Wszystkie przestępstwa narkotykowe — posiadanie, obrót, wytwarzanie.
    3. Tak, szczególnie przepisy o zawieszeniu kary i warunkowym umorzeniu.
    4. Wyroki skazujące i warunkowe umorzenia. Uniewinnienia nie.
    5. Tak, to ważna zmienna — chcę te kategorie. Dodatkowo chcę też podzielić wiek oskarżonego na 5 przedziałów wiekowych.
    6. Tak, wszystkie te okoliczności są ważne.
    7. Tak, ilość i rodzaj środka są ważne. Cel też.
    8. Nie, nie interesuje mnie zmiana orzecznictwa w czasie.
    9. Nie, nie chcę tego wyodrębniać, bo taka informacja będzie już zawarta w wieku oskarżonego. Równoległe czyny też chciałbym przeanalizować, ponieważ mogą wpływać na wymiar kary.


    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Asystent</span>

    Badamy zależność między wiekiem oskarżonego a rodzajem i surowością kary w sprawach o przestępstwa narkotykowe (posiadanie, obrót, wytwarzanie), obejmując wyroki skazujące i warunkowe umorzenia, z podziałem na nieletniego, młodocianego i dorosłego oraz na pięć przedziałów wiekowych. Uwzględniamy też ilość i rodzaj substancji, cel działania, zawieszenie kary oraz okoliczności łagodzące i obciążające (karalność, recydywę, współsprawstwo, cel majątkowy). Podstawą prawną są ustawa o przeciwdziałaniu narkomanii oraz Kodeks karny; uniewinnienia i zmiany linii orzeczniczej w czasie są poza zakresem.

    </div>
    <div class="chat-msg chat-assistant" markdown="1">
    <span class="chat-label">Asystent</span>

    Na podstawie Twojego zapytania przygotowałem schemat ekstrakcji do analizy polskich orzeczeń sądowych w sprawach o przestępstwa narkotykowe, z naciskiem na to, jak wiek oskarżonego wpływa na rodzaj i surowość reakcji karnej. Ująłem w nim wyroki skazujące oraz wyroki warunkowo umarzające postępowanie, bez uniewinnień, a także rozróżnienie między nieletnim, młodocianym i dorosłym oraz podział wieku na 5 przedziałów.

    Obecny schemat obejmuje trzy główne obszary: dane o dokumencie i sprawie, dane o oskarżonym oraz dane o czynie i karze. Wydobywa m.in. typ dokumentu, rolę i źródło informacji w orzeczeniu, kwalifikację prawną czynu, rodzaj przestępstwa narkotykowego, ilość i kategorię substancji, cel działania, wiek oskarżonego w chwili czynu i orzekania, a także rodzaj kary, jej wysokość, zawieszenie, warunkowe umorzenie, okres próby, podstawy prawne oraz okoliczności łagodzące i obciążające. Dodatkowo uwzględnia wcześniejszą karalność, recydywę, uzależnienie, działanie dla korzyści majątkowej, współsprawstwo i równoległe czyny zabronione.

    Schemat jest więc dopasowany do analizy, czy i jak wiek oraz kontekst sprawy wiążą się z surowością kary w sprawach narkotykowych. Jeśli chcesz, możesz teraz wskazać, co mamy jeszcze doprecyzować, uprościć albo dodać.

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

    **122 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `document_id` | string | Technical identifier of the record or document in the corpus. Extracted from source metadata; not constructed from the ruling's content. |
        | `record_unit` | enum | The analytical unit represented by the record — the whole document, a single defendant, a defendant and the main drug offense, or a defendant and an underlying case. |
        | `source_document_kind` | enum | Type of source document available, relevant to the completeness of age, drug-quantity, and sentence data. |
        | `proceeding_type` | enum | High-level (partly legacy) classification of the type of proceeding or ruling. Used for coarse corpus filtering; finer stage and decision form are coded separately. |
        | `document_procedural_stage` | enum | Procedural stage of the analyzed document. |
        | `decision_form` | enum | Formal form of the court's decision (judgment, order, etc.). |
        | `document_relevance_for_study` | enum | Overall usefulness of the document for studying the age-sentence relationship in drug offenses. |
        | `exclusion_reason_primary` | enum | Main reason for excluding the document from the core age/sentence analysis. |
        | `usable_for_age_vs_sentence_analysis` | enum | Whether the document reliably allows the defendant's age to be compared against the type or severity of the sentence. |
        | `usable_for_drug_quantity_analysis` | enum | Whether the document reliably allows analysis of the drug type and quantity and their relation to the ruling. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `document_id` | string | Znaczenie: techniczny identyfikator rekordu lub dokumentu w korpusie. Typ: string. Wymagalność: false. Ekstrakcja: przejmij z metadanych źródła; nie twórz z treści orzeczenia. |
        | `record_unit` | enum | Znaczenie: jednostka analizy reprezentowana przez rekord. Typ: enum. Wymagalność: true. Ekstrakcja: ustal, czy rekord opisuje cały dokument, jednego oskarżonego, oskarżonego i główny czyn narkotykowy, czy oskarżonego i sprawę bazową; pole ogranicza niejednoznaczność przy wielu oskarżonych, czynach i sprawach bazowych. |
        | `source_document_kind` | enum | Znaczenie: rodzaj dostępnego dokumentu źródłowego, istotny dla kompletności danych o wieku, ilości narkotyku i karze. Typ: enum. Wymagalność: true. Ekstrakcja: rozpoznaj z nagłówka i struktury dokumentu; dla dokumentów wykonawczych lub postanowień użyj najbardziej precyzyjnej wartości. |
        | `proceeding_type` | enum | Znaczenie: wysokopoziomowa, częściowo legacy, klasyfikacja rodzaju postępowania lub rozstrzygnięcia. Typ: enum. Wymagalność: true. Ekstrakcja: używaj do zgrubnego filtrowania korpusu; dokładniejszy etap i forma decyzji są kodowane osobno w `document_procedural_stage`, `decision_form` i `postpenal_decision_type`. |
        | `document_procedural_stage` | enum | Znaczenie: etap proceduralny, którego dotyczy analizowany dokument. Typ: enum. Wymagalność: true. Ekstrakcja: ustal z nagłówka, sygnatury, treści sentencji i charakteru rozstrzygnięcia. |
        | `decision_form` | enum | Znaczenie: formalna postać decyzji sądu. Typ: enum. Wymagalność: true. Ekstrakcja: szukaj słów 'wyrok', 'postanowienie' lub 'zarządzenie' w nagłówku dokumentu. |
        | `document_relevance_for_study` | enum | Znaczenie: ogólna przydatność dokumentu do badania związku wieku sprawcy z karą za czyn narkotykowy. Typ: enum. Wymagalność: true. |
        | `exclusion_reason_primary` | enum | Znaczenie: główny powód wyłączenia dokumentu z analizy rdzeniowej wieku i kary. Typ: enum. Wymagalność: true. Ekstrakcja: wypełniaj także dla dokumentów potencjalnie przydatnych; jeśli brak podstaw do wyłączenia użyj `brak`. |
        | `usable_for_age_vs_sentence_analysis` | enum | Znaczenie: czy dokument pozwala wiarygodnie zestawić wiek sprawcy z rodzajem lub wysokością reakcji karnej. Typ: enum. Wymagalność: true. Ekstrakcja: uwzględnij kompletność danych o wieku, karze i związku kary z czynem narkotykowym. |
        | `usable_for_drug_quantity_analysis` | enum | Znaczenie: czy dokument pozwala wiarygodnie analizować rodzaj i ilość substancji oraz ich związek z rozstrzygnięciem. Typ: enum. Wymagalność: true. |
    ??? note "Show full schema (122 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: techniczny identyfikator rekordu lub dokumentu w korpusie. Typ: string. Wymagalność: false. Ekstrakcja: przejmij z metadanych źródła; nie twórz z treści orzeczenia.",
            "name": "document_id"
          },
          {
            "type_": "enum",
            "enum_name": "RecordUnit",
            "enum_values": [
              "dokument",
              "oskarzony",
              "oskarzony_i_glowny_czyn_narkotykowy",
              "oskarzony_i_sprawa_bazowa",
              "nieustalone"
            ],
            "description": "Znaczenie: jednostka analizy reprezentowana przez rekord. Typ: enum. Wymagalność: true. Ekstrakcja: ustal, czy rekord opisuje cały dokument, jednego oskarżonego, oskarżonego i główny czyn narkotykowy, czy oskarżonego i sprawę bazową; pole ogranicza niejednoznaczność przy wielu oskarżonych, czynach i sprawach bazowych.",
            "name": "record_unit"
          },
          {
            "type_": "enum",
            "enum_name": "SourceDocumentKind",
            "enum_values": [
              "uzasadnienie",
              "sentencja",
              "wyrok_z_uzasadnieniem",
              "postanowienie",
              "postanowienie_z_uzasadnieniem",
              "orzeczenie_wykonawcze",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: rodzaj dostępnego dokumentu źródłowego, istotny dla kompletności danych o wieku, ilości narkotyku i karze. Typ: enum. Wymagalność: true. Ekstrakcja: rozpoznaj z nagłówka i struktury dokumentu; dla dokumentów wykonawczych lub postanowień użyj najbardziej precyzyjnej wartości.",
            "name": "source_document_kind"
          },
          {
            "type_": "enum",
            "enum_name": "ProceedingType",
            "enum_values": [
              "wyrok_skazujacy",
              "warunkowe_umorzenie",
              "wyrok_laczny",
              "apelacyjne",
              "postepowanie_wykonawcze",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: wysokopoziomowa, częściowo legacy, klasyfikacja rodzaju postępowania lub rozstrzygnięcia. Typ: enum. Wymagalność: true. Ekstrakcja: używaj do zgrubnego filtrowania korpusu; dokładniejszy etap i forma decyzji są kodowane osobno w `document_procedural_stage`, `decision_form` i `postpenal_decision_type`.",
            "name": "proceeding_type"
          },
          {
            "type_": "enum",
            "enum_name": "DocumentProceduralStage",
            "enum_values": [
              "I_instancja_meritum",
              "II_instancja_odwolawcza",
              "postepowanie_wykonawcze",
              "wyrok_laczny",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: etap proceduralny, którego dotyczy analizowany dokument. Typ: enum. Wymagalność: true. Ekstrakcja: ustal z nagłówka, sygnatury, treści sentencji i charakteru rozstrzygnięcia.",
            "name": "document_procedural_stage"
          },
          {
            "type_": "enum",
            "enum_name": "DecisionForm",
            "enum_values": [
              "wyrok",
              "postanowienie",
              "zarzadzenie",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: formalna postać decyzji sądu. Typ: enum. Wymagalność: true. Ekstrakcja: szukaj słów 'wyrok', 'postanowienie' lub 'zarządzenie' w nagłówku dokumentu.",
            "name": "decision_form"
          },
          {
            "type_": "enum",
            "enum_name": "StudyRelevance",
            "enum_values": [
              "bezposrednio_przydatny",
              "posrednio_przydatny",
              "do_wykluczenia",
              "nieustalone"
            ],
            "description": "Znaczenie: ogólna przydatność dokumentu do badania związku wieku sprawcy z karą za czyn narkotykowy. Typ: enum. Wymagalność: true.",
            "name": "document_relevance_for_study"
          },
          {
            "type_": "enum",
            "enum_name": "ExclusionReasonPrimary",
            "enum_values": [
              "brak",
              "dokument_wykonawczy",
              "brak_danych_o_wieku",
              "brak_opisu_czynu_narkotykowego",
              "kara_nieodnosi_sie_bezposrednio_do_czynu",
              "dane_tylko_o_sprawie_bazowej",
              "uniewinnienie_lub_brak_skazania",
              "poza_zakresem_przestepstw_narkotykowych",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: główny powód wyłączenia dokumentu z analizy rdzeniowej wieku i kary. Typ: enum. Wymagalność: true. Ekstrakcja: wypełniaj także dla dokumentów potencjalnie przydatnych; jeśli brak podstaw do wyłączenia użyj `brak`.",
            "name": "exclusion_reason_primary"
          },
          {
            "type_": "enum",
            "enum_name": "UsabilityFlag",
            "enum_values": [
              "tak",
              "nie",
              "czesciowo",
              "nieustalone"
            ],
            "description": "Znaczenie: czy dokument pozwala wiarygodnie zestawić wiek sprawcy z rodzajem lub wysokością reakcji karnej. Typ: enum. Wymagalność: true. Ekstrakcja: uwzględnij kompletność danych o wieku, karze i związku kary z czynem narkotykowym.",
            "name": "usable_for_age_vs_sentence_analysis"
          },
          {
            "type_": "enum",
            "enum_name": "UsabilityFlag",
            "enum_values": [
              "tak",
              "nie",
              "czesciowo",
              "nieustalone"
            ],
            "description": "Znaczenie: czy dokument pozwala wiarygodnie analizować rodzaj i ilość substancji oraz ich związek z rozstrzygnięciem. Typ: enum. Wymagalność: true.",
            "name": "usable_for_drug_quantity_analysis"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: sygnatura akt analizowanego orzeczenia w brzmieniu z dokumentu. Typ: string. Wymagalność: false. Ekstrakcja: zwykle w nagłówku lub pierwszych liniach.",
            "name": "case_number"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: pełna nazwa sądu, który wydał analizowane orzeczenie. Typ: string. Wymagalność: false. Ekstrakcja: szukaj w nagłówku sentencji lub uzasadnienia.",
            "name": "court_name"
          },
          {
            "type_": "enum",
            "enum_name": "CourtInstance",
            "enum_values": [
              "I_instancja",
              "II_instancja",
              "nieustalone"
            ],
            "description": "Znaczenie: instancja sądu dla analizowanego orzeczenia. Typ: enum. Wymagalność: true.",
            "name": "court_instance"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: data wydania analizowanego orzeczenia, najlepiej w formacie RRRR-MM-DD. Typ: string. Wymagalność: false. Ekstrakcja: zapisuj tylko datę możliwą do jednoznacznej standaryzacji.",
            "name": "judgment_date"
          },
          {
            "type_": "enum",
            "enum_name": "AppellateDisposition",
            "enum_values": [
              "utrzymano_w_mocy",
              "zmieniono",
              "uchylono_i_przekazano",
              "uchylono_i_umorzono",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Znaczenie: sposób rozstrzygnięcia środka odwoławczego. Typ: enum. Wymagalność: true. Dla orzeczeń I instancji użyj `nie_dotyczy`.",
            "name": "appellate_disposition"
          },
          {
            "type_": "enum",
            "enum_name": "PostpenalDecisionType",
            "enum_values": [
              "nie_dotyczy",
              "warunkowe_przedterminowe_zwolnienie",
              "odmowa_warunkowego_przedterminowego_zwolnienia",
              "przerwa_w_karze",
              "odroczenie_wykonania",
              "zarzadzenie_wykonania_kary",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: szczegółowy typ decyzji w postępowaniu wykonawczym lub postpenalnym. Typ: enum. Wymagalność: true. Ekstrakcja: wypełniaj przede wszystkim przy `document_procedural_stage = postepowanie_wykonawcze`; w innych przypadkach użyj `nie_dotyczy`.",
            "name": "postpenal_decision_type"
          },
          {
            "type_": "enum",
            "enum_name": "FactsSourceLevel",
            "enum_values": [
              "sentencja_biezacej_sprawy",
              "uzasadnienie_biezacej_sprawy",
              "opis_wczesniejszego_wyroku",
              "brak",
              "nieustalone"
            ],
            "description": "Znaczenie: poziom źródła, z którego pochodzą ustalenia o czynie narkotykowym i karze. Typ: enum. Wymagalność: true. Kluczowe dla dokumentów pośrednich.",
            "name": "facts_source_level"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy dokument łączy lub omawia więcej niż jedną sprawę bazową istotną dla końcowej kary. Typ: enum. Wymagalność: true.",
            "name": "multiple_underlying_cases_combined"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: liczba spraw bazowych opisanych lub przywołanych w dokumencie, o ile da się ją ustalić. Typ: integer. Wymagalność: false.",
            "name": "underlying_cases_count"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: ustrukturyzowany opis spraw bazowych istotnych dla rekordu. Typ: string. Wymagalność: false. Ekstrakcja: zapisuj jeden segment na sprawę w formacie `case_number=... | judgment_date=... | is_drug_offense=tak/nie/nieustalone | sentence_scope=reakcja_koncowa_wobec_oskarzonego/kara_za_glowny_czyn_narkotykowy/kara_laczna/kara_w_sprawie_bazowej_opisana_posrednio/nieustalone | case_role=sprawa_bazowa/sprawa_laczona/sprawa_opisana_posrednio/inna`; segmenty oddzielaj średnikiem.",
            "name": "underlying_cases_structured_text"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: opis spraw bazowych istotnych dla rekordu w formie tekstowej pomocniczej. Typ: string. Wymagalność: false. Ekstrakcja: jeśli pole jest używane, zachowuj stały porządek `sygnatura | data | czy_narkotykowa | rola_sprawy | uwaga`; wiele spraw oddzielaj średnikiem.",
            "name": "underlying_cases_summary"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: data wyroku I instancji w sprawie bazowej, jeśli dokument pośredni ją podaje i może pomagać ustalić status młodocianego. Typ: string. Wymagalność: false.",
            "name": "underlying_first_instance_judgment_date"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: oznaczenie oskarżonego lub sprawcy, którego dotyczy rekord, np. inicjały albo numer porządkowy. Typ: string. Wymagalność: false.",
            "name": "defendant_label"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy analizowane orzeczenie obejmuje więcej niż jednego oskarżonego lub sprawcę. Typ: enum. Wymagalność: true.",
            "name": "judgment_covers_multiple_defendants"
          },
          {
            "type_": "enum",
            "enum_name": "CaseOutcome",
            "enum_values": [
              "skazanie",
              "warunkowe_umorzenie",
              "wyrok_laczny",
              "rozstrzygniecie_odwolawcze",
              "warunkowe_przedterminowe_zwolnienie",
              "odmowa_warunkowego_przedterminowego_zwolnienia",
              "decyzja_wykonawcza",
              "mieszane_wobec_wielu_czynow",
              "inne_procesowe",
              "nieustalone"
            ],
            "description": "Znaczenie: końcowy wynik wobec tego oskarżonego w analizowanym dokumencie. Typ: enum. Wymagalność: true. Ekstrakcja: dla dokumentów wykonawczych używaj wartości szczególnej lub ogólnej `decyzja_wykonawcza` zamiast wymuszać `inne_procesowe`.",
            "name": "case_outcome"
          },
          {
            "type_": "enum",
            "enum_name": "SentenceDrugRelation",
            "enum_values": [
              "tak",
              "nie",
              "czesciowo",
              "nieustalone"
            ],
            "description": "Znaczenie: czy opisana kara lub reakcja prawna odnosi się bezpośrednio do czynu narkotykowego. Typ: enum. Wymagalność: true.",
            "name": "sentence_relates_directly_to_drug_offense"
          },
          {
            "type_": "enum",
            "enum_name": "SentenceIdentifiable",
            "enum_values": [
              "tak",
              "nie",
              "czesciowo",
              "nieustalone"
            ],
            "description": "Znaczenie: czy z dokumentu da się wyodrębnić karę za sam czyn narkotykowy, odrębnie od kary łącznej lub szerszego rozstrzygnięcia. Typ: enum. Wymagalność: true. To pole chroni przed myleniem kary łącznej z karą za czyn narkotykowy.",
            "name": "drug_offense_sentence_identifiable"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy dokument wprost opisuje czyn narkotykowy, jego kwalifikację i ustalenia faktyczne, zamiast tylko odwoływać się do wcześniejszego wyroku. Typ: enum. Wymagalność: true.",
            "name": "drug_offense_described_directly_in_document"
          },
          {
            "type_": "enum",
            "enum_name": "LiabilityRegime",
            "enum_values": [
              "prawo_karne_doroslych",
              "postepowanie_w_sprawie_nieletniego",
              "nieustalone"
            ],
            "description": "Znaczenie: reżim odpowiedzialności lub postępowania zastosowany wobec sprawcy. Typ: enum. Wymagalność: true.",
            "name": "liability_regime"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sprawa została rozpoznana z użyciem trybu konsensualnego wpływającego na treść rozstrzygnięcia. Typ: enum. Wymagalność: true. Przykłady: art. 335 k.p.k., art. 387 k.p.k.",
            "name": "consensual_procedure_applied"
          },
          {
            "type_": "enum",
            "enum_name": "ProceduralMode",
            "enum_values": [
              "art_335",
              "art_387",
              "zwykly_tryb",
              "wyrok_laczny",
              "postepowanie_odwolawcze",
              "postepowanie_wykonawcze",
              "nie_dotyczy",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: główny tryb proceduralny rozpoznania sprawy. Typ: enum. Wymagalność: true. Ekstrakcja: w dokumentach takich jak wyrok łączny lub postępowanie wykonawcze użyj odpowiedniej wartości zamiast `zwykly_tryb`.",
            "name": "procedural_mode"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: dokładna data popełnienia głównego czynu narkotykowego, jeśli dokument wskazuje jeden dzień czynu. Typ: string. Wymagalność: false. Kluczowe do ustalenia wieku w chwili czynu.",
            "name": "offense_date"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: początek okresu popełniania czynu, gdy czyn był rozciągnięty w czasie lub wskazano przedział dat. Typ: string. Wymagalność: false.",
            "name": "offense_period_start"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: koniec okresu popełniania czynu, gdy czyn był rozciągnięty w czasie lub wskazano przedział dat. Typ: string. Wymagalność: false.",
            "name": "offense_period_end"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wiek sprawcy w pełnych latach w chwili popełnienia głównego czynu narkotykowego. Typ: integer. Wymagalność: false. Ekstrakcja: ustalaj przede wszystkim z daty czynu lub początku okresu czynu; nie zgaduj przy braku podstaw.",
            "name": "age_at_offense_years"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wiek sprawcy w pełnych latach w chwili wyroku I instancji, jeśli dokument pośredni lub bazowy daje podstawę do ustalenia. Typ: integer. Wymagalność: false. Pole pomocnicze dla statusu młodocianego.",
            "name": "age_at_first_instance_years"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wiek sprawcy w pełnych latach w chwili wydania analizowanego orzeczenia. Typ: integer. Wymagalność: false.",
            "name": "age_at_judgment_years"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: legacy coarse flag wskazujący, czy dostępny jest rok urodzenia lub inna informacja pozwalająca go pewnie ustalić. Typ: enum. Wymagalność: true. Ekstrakcja: interpretuj łącznie z `birth_info_status`, które rozróżnia brak danych od anonimizacji.",
            "name": "birth_year_available"
          },
          {
            "type_": "enum",
            "enum_name": "BirthInfoStatus",
            "enum_values": [
              "dostepne",
              "zanonimizowane",
              "brak",
              "nieustalone"
            ],
            "description": "Znaczenie: status danych o dacie lub roku urodzenia oskarżonego. Typ: enum. Wymagalność: true. Ekstrakcja: użyj `zanonimizowane`, gdy dokument sugeruje istnienie danych, ale publikacja je ukrywa; `brak`, gdy dokument nie podaje takich danych w ogóle.",
            "name": "birth_info_status"
          },
          {
            "type_": "enum",
            "enum_name": "AgeConfidence",
            "enum_values": [
              "wysoka",
              "srednia",
              "niska",
              "brak"
            ],
            "description": "Znaczenie: ocena pewności ustalenia wieku użytego w polach wiekowych. Typ: enum. Wymagalność: true.",
            "name": "age_confidence"
          },
          {
            "type_": "enum",
            "enum_name": "AgeDeterminationSource",
            "enum_values": [
              "wprost_wskazany",
              "wyliczony_z_daty_urodzenia_i_daty_czynu",
              "wyliczony_z_daty_urodzenia_i_daty_orzeczenia",
              "wprost_wskazany_wiek_w_chwili_orzeczenia",
              "wyliczony_z_innych_dat_sprawy",
              "oszacowany_z_opisu",
              "nieustalone"
            ],
            "description": "Znaczenie: sposób ustalenia wieku użytego w polach wiekowych. Typ: enum. Wymagalność: true. Rozszerzone o sytuacje typowe dla dokumentów pośrednich.",
            "name": "age_determination_source"
          },
          {
            "type_": "enum",
            "enum_name": "OffenderAgeLegalCategory",
            "enum_values": [
              "nieletni",
              "mlodociany",
              "dorosly",
              "nieustalone"
            ],
            "description": "Znaczenie: kategoria prawna sprawcy z perspektywy wieku. Typ: enum. Wymagalność: warunkowa; gdy brak podstaw użyj `nieustalone`.",
            "name": "offender_age_legal_category"
          },
          {
            "type_": "enum",
            "enum_name": "OffenderAgeLegalCategoryBasis",
            "enum_values": [
              "wprost_wskazana_przez_sad",
              "ustalona_z_definicji_prawnej",
              "nieustalone"
            ],
            "description": "Znaczenie: podstawa ustalenia pola `offender_age_legal_category`. Typ: enum. Wymagalność: true.",
            "name": "offender_age_legal_category_basis"
          },
          {
            "type_": "enum",
            "enum_name": "AgeBand5",
            "enum_values": [
              "do_16",
              "17_20",
              "21_24",
              "25_34",
              "35_plus",
              "nieustalone"
            ],
            "description": "Znaczenie: pięcioprzedziałowa kategoria wieku do analiz statystycznych, ustalana przede wszystkim według wieku w chwili czynu. Typ: enum. Wymagalność: warunkowa; przy braku danych użyj `nieustalone`.",
            "name": "age_band_5"
          },
          {
            "type_": "enum",
            "enum_name": "AgeBandBasis",
            "enum_values": [
              "wiek_w_chwili_czynu",
              "wiek_w_chwili_orzeczenia",
              "wiek_w_chwili_wyroku_I_instancji",
              "nieustalone"
            ],
            "description": "Znaczenie: wskazuje, na jakiej podstawie ustalono `age_band_5`. Typ: enum. Wymagalność: true.",
            "name": "age_band_basis"
          },
          {
            "type_": "enum",
            "enum_name": "AgeReferenceMention",
            "enum_values": [
              "tak",
              "brak_wzmianki",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd wprost odwołał się do wieku sprawcy przy uzasadnianiu rodzaju lub wysokości kary albo warunkowego umorzenia. Typ: enum. Wymagalność: true.",
            "name": "court_explicitly_referenced_age_in_sentencing"
          },
          {
            "type_": "enum",
            "enum_name": "AgeReferenceEffect",
            "enum_values": [
              "lagodzaca",
              "obciazajaca",
              "neutralna",
              "mieszana",
              "brak_wzmianki",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Znaczenie: znaczenie przypisane wiekowi sprawcy w argumentacji sądu. Typ: enum. Wymagalność: true.",
            "name": "age_reference_effect"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: cytat albo wierny skrót fragmentu uzasadnienia, w którym sąd odnosi się do wieku sprawcy przy ocenie kary lub środka probacyjnego. Typ: string. Wymagalność: false.",
            "name": "age_reference_excerpt"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy uzasadnienie zawiera wystarczające motywy dotyczące wymiaru kary lub środka probacyjnego do kodowania okoliczności łagodzących i obciążających. Typ: enum. Wymagalność: true.",
            "name": "sentencing_reasoning_present"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: przepisy ustawy o przeciwdziałaniu narkomanii stanowiące podstawę kwalifikacji czynu przypisanego temu oskarżonemu. Typ: string. Wymagalność: false. Ekstrakcja: zapisuj jako zwykły tekst rozdzielony średnikami, np. `art. 62 ust. 1 u.p.n.; art. 59 ust. 1 u.p.n.`.",
            "name": "drug_offense_articles_text"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd przyjął czyn ciągły, ciąg przestępstw albo inną konstrukcję ciągłości zachowania mogącą wpływać na kwalifikację lub karę. Typ: enum. Wymagalność: true.",
            "name": "continuous_offense_applied"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: liczba odrębnych czynów narkotykowych przypisanych temu oskarżonemu, o ile da się ją ustalić. Typ: integer. Wymagalność: false.",
            "name": "number_of_drug_counts"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: główny przepis czynu narkotykowego najbardziej istotnego dla analizy wymiaru kary. Typ: string. Wymagalność: false.",
            "name": "primary_drug_offense_article"
          },
          {
            "type_": "enum",
            "enum_name": "PrimaryDrugOffenseType",
            "enum_values": [
              "posiadanie",
              "udzielanie_niekomercyjne",
              "sprzedaz_lub_odplatne_udzielanie",
              "wprowadzanie_do_obrotu_lub_obrot",
              "wytwarzanie_przetwarzanie_produkcja",
              "uprawa",
              "przewoz_przemyt_import_eksport",
              "inne",
              "mieszane",
              "niejednoznaczne",
              "nieustalone"
            ],
            "description": "Znaczenie: główny znormalizowany typ zachowania narkotykowego przypisanego oskarżonemu. Typ: enum. Wymagalność: true.",
            "name": "primary_drug_offense_type"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy oskarżonemu przypisano posiadanie narkotyków jako jeden z czynów lub element kwalifikacji. Typ: enum. Wymagalność: true.",
            "name": "offense_possession"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy przypisano udzielanie, częstowanie albo inne przekazanie narkotyku innej osobie bez wyraźnego ustalenia komercyjnego charakteru. Typ: enum. Wymagalność: true.",
            "name": "offense_supply_noncommercial"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy przypisano sprzedaż, odpłatne udzielanie, dystrybucję handlową albo inny komercyjny obrót narkotykami. Typ: enum. Wymagalność: true.",
            "name": "offense_sale_or_commercial_distribution"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy przypisano wytwarzanie, przetwarzanie, produkcję lub podobną działalność dotyczącą narkotyków. Typ: enum. Wymagalność: true.",
            "name": "offense_manufacturing_or_processing"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy przypisano uprawę roślin związanych z produkcją narkotyków. Typ: enum. Wymagalność: true.",
            "name": "offense_cultivation"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy przypisano przemyt, przewóz transgraniczny, import albo eksport narkotyków. Typ: enum. Wymagalność: true.",
            "name": "offense_import_export_or_smuggling"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy występuje inny typ przestępstwa narkotykowego niewyrażony w powyższych polach. Typ: enum. Wymagalność: true.",
            "name": "other_drug_offense_present"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy obok czynu lub czynów narkotykowych występowały inne czyny z innych przepisów niż ustawa o przeciwdziałaniu narkomanii. Typ: enum. Wymagalność: true.",
            "name": "cooccurring_offenses_present"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: liczba odrębnych czynów współwystępujących z innych przepisów przypisanych temu oskarżonemu, o ile da się ją ustalić. Typ: integer. Wymagalność: false.",
            "name": "number_of_cooccurring_counts"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: przepisy dotyczące czynów współwystępujących przypisanych temu oskarżonemu. Typ: string. Wymagalność: false. Ekstrakcja: zapisuj w formacie listy rozdzielanej średnikami, np. `art. 178a § 1 k.k.; art. 157 § 2 k.k.`.",
            "name": "cooccurring_offenses_articles_text"
          },
          {
            "type_": "enum",
            "enum_name": "CooccurringOffensesAffectedSentence",
            "enum_values": [
              "tak",
              "nie",
              "brak_wzmianki",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Znaczenie: czy z sentencji lub uzasadnienia wynika, że czyny współwystępujące realnie wpłynęły na końcowy wymiar kary, karę łączną albo wybór reakcji karnej. Typ: enum. Wymagalność: true.",
            "name": "cooccurring_offenses_affected_sentence"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: ustrukturyzowany opis jednej lub wielu substancji i ich ilości. Typ: string. Wymagalność: false. Ekstrakcja: zapisuj jeden segment na substancję w formacie `drug_name=... | quantity_value=... | quantity_unit=gram/kilogram/sztuki/porcje/tabletki/krzewy/mililitr/inne/nieustalone | measurement_basis=masa/porcje_handlowe/liczba_sztuk_lub_tabletek/liczba_roslin/objetosc/inne/nieustalone | quantity_category=znaczna_ilosc/inna_wprost_wskazana/brak_wyraznej_kategorii/nieustalone | is_primary=tak/nie`; segmenty oddzielaj średnikiem.",
            "name": "drug_items_structured_text"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: tekstowy opis substancji i ich ilości w brzmieniu z orzeczenia lub wiernym skrócie. Typ: string. Wymagalność: false. Ekstrakcja: jeśli używasz pola do strukturyzacji ręcznej, zachowuj stały porządek `nazwa | ilosc | jednostka | podstawa_pomiaru | kategoria_ilosci`; wiele pozycji oddzielaj średnikiem.",
            "name": "drug_items_text"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: tekstowy opis wszystkich rodzajów środków odurzających, substancji psychotropowych lub nowych substancji psychoaktywnych przypisanych temu oskarżonemu. Typ: string. Wymagalność: false.",
            "name": "drug_types_all_text"
          },
          {
            "type_": "enum",
            "enum_name": "DrugTypePrimary",
            "enum_values": [
              "marihuana",
              "haszysz",
              "amfetamina",
              "metamfetamina",
              "kokaina",
              "heroina",
              "mdma_ecstasy",
              "opioidy_inne_niz_heroina",
              "nowa_substancja_psychoaktywna",
              "mieszane",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: główny rodzaj substancji dla celów porównawczych; przy kilku równorzędnych substancjach użyj `mieszane`. Typ: enum. Wymagalność: true. Pole pomocnicze; pełniejszy obraz wielosubstancyjności koduj w `drug_items_structured_text`.",
            "name": "drug_type_primary"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sprawa dotyczyła więcej niż jednego rodzaju substancji. Typ: enum. Wymagalność: true.",
            "name": "has_multiple_drug_types"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: liczba rodzajów substancji przypisanych temu oskarżonemu, o ile da się ją ustalić. Typ: integer. Wymagalność: false.",
            "name": "number_of_drug_types"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: surowy opis ilości substancji z orzeczenia, zachowany w oryginalnym brzmieniu lub wiernym skrócie. Typ: string. Wymagalność: false. To pole jest ważne, gdy dokument nie daje jednego jednoznacznego pomiaru.",
            "name": "drug_quantity_raw_text"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: jedna liczbowo wyrażona ilość substancji wskazana w orzeczeniu. Typ: float. Wymagalność: false. Wypełniaj tylko wtedy, gdy można jednoznacznie przypisać pojedynczą wartość do pola agregacyjnego; przy wielu substancjach lub wielu jednostkach preferuj `drug_items_structured_text`.",
            "name": "drug_quantity_value"
          },
          {
            "type_": "enum",
            "enum_name": "DrugQuantityUnit",
            "enum_values": [
              "gram",
              "kilogram",
              "sztuki",
              "porcje",
              "tabletki",
              "krzewy",
              "mililitr",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: jednostka miary użyta przy oznaczeniu ilości substancji w polu agregacyjnym `drug_quantity_value`. Typ: enum. Wymagalność: warunkowa; gdy brak jednej liczby użyj `nieustalone`.",
            "name": "drug_quantity_unit"
          },
          {
            "type_": "enum",
            "enum_name": "DrugQuantityCategory",
            "enum_values": [
              "znaczna_ilosc",
              "inna_wprost_wskazana",
              "brak_wyraznej_kategorii",
              "nieustalone"
            ],
            "description": "Znaczenie: kategoria ilości narkotyku wynikająca wprost z ustaleń sądu lub z kwalifikacji prawnej. Typ: enum. Wymagalność: warunkowa.",
            "name": "drug_quantity_category"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd wprost ustalił albo kwalifikacja prawna wyraźnie implikuje, że chodzi o znaczną ilość narkotyku. Typ: enum. Wymagalność: true.",
            "name": "significant_quantity_found"
          },
          {
            "type_": "enum",
            "enum_name": "QuantityReferenceScope",
            "enum_values": [
              "glownej_substancji",
              "sumy_wszystkich_substancji",
              "nieustalone"
            ],
            "description": "Znaczenie: określa, do czego odnosi się `drug_quantity_value`: do głównej substancji czy do łącznej ilości wszystkich substancji. Typ: enum. Wymagalność: warunkowa.",
            "name": "quantity_refers_to"
          },
          {
            "type_": "enum",
            "enum_name": "DrugQuantityMeasurementBasis",
            "enum_values": [
              "masa",
              "porcje_handlowe",
              "liczba_sztuk_lub_tabletek",
              "liczba_roslin",
              "objetosc",
              "inne",
              "nieustalone"
            ],
            "description": "Znaczenie: wskazuje, jaki sposób pomiaru stoi za `drug_quantity_value`. Typ: enum. Wymagalność: warunkowa.",
            "name": "drug_quantity_measurement_basis"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy z ustaleń sądu wynika, że posiadanie lub działanie sprawcy było związane z własnym użyciem. Typ: enum. Wymagalność: true.",
            "name": "purpose_own_use"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy z ustaleń sądu wynika zamiar udzielenia, przekazania lub dostarczenia narkotyku innej osobie, niezależnie od motywu majątkowego. Typ: enum. Wymagalność: true.",
            "name": "intent_to_supply_or_share"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy czyn był osadzony w kontekście obrotu, sprzedaży lub dystrybucji handlowej. Typ: enum. Wymagalność: true.",
            "name": "commercial_trafficking_context"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd ustalił działanie w celu osiągnięcia korzyści majątkowej. Typ: enum. Wymagalność: true.",
            "name": "profit_motive"
          },
          {
            "type_": "enum",
            "enum_name": "BenefitMotiveType",
            "enum_values": [
              "majatkowa",
              "osobista",
              "obie",
              "brak",
              "nieustalone"
            ],
            "description": "Znaczenie: znormalizowany typ korzyści lub motywu przypisanego działaniu sprawcy. Typ: enum. Wymagalność: true.",
            "name": "benefit_motive_type"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy na dzień popełnienia czynu sąd wskazał uprzednią karalność sprawcy w jakiejkolwiek postaci. Typ: enum. Wymagalność: true.",
            "name": "prior_conviction_at_offense_time"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy na dzień wydania orzeczenia sąd wskazał uprzednią karalność sprawcy w jakiejkolwiek postaci. Typ: enum. Wymagalność: true.",
            "name": "prior_conviction_at_judgment_time"
          },
          {
            "type_": "enum",
            "enum_name": "PriorSimilarConvictionStatus",
            "enum_values": [
              "tak",
              "nie",
              "brak_wzmianki",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Znaczenie: czy na dzień popełnienia czynu sąd wskazał uprzednią karalność za przestępstwa podobne lub zbliżone rodzajowo, zwłaszcza narkotykowe. Typ: enum. Wymagalność: true.",
            "name": "prior_conviction_for_similar_offense_at_offense_time"
          },
          {
            "type_": "enum",
            "enum_name": "PriorSimilarConvictionStatus",
            "enum_values": [
              "tak",
              "nie",
              "brak_wzmianki",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Znaczenie: czy na dzień wydania orzeczenia sąd wskazał uprzednią karalność za przestępstwa podobne lub zbliżone rodzajowo, zwłaszcza narkotykowe. Typ: enum. Wymagalność: true.",
            "name": "prior_conviction_for_similar_offense_at_judgment_time"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy wobec sprawcy zastosowano albo wprost rozważano recydywę ustawową jako podstawę prawną lub element kwalifikacji. Typ: enum. Wymagalność: true.",
            "name": "statutory_recidivism_applied"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy z uzasadnienia wynika uzależnienie sprawcy od narkotyków, alkoholu lub innych substancji w stopniu uznanym przez sąd za istotny. Typ: enum. Wymagalność: true.",
            "name": "addiction_noted"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy czyn został popełniony we współsprawstwie lub wspólnie z innymi osobami. Typ: enum. Wymagalność: true.",
            "name": "co_perpetration"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sprawca przyznał się do winy lub do popełnienia czynu w zakresie istotnym dla rozstrzygnięcia. Typ: enum. Wymagalność: true.",
            "name": "confession"
          },
          {
            "type_": "enum",
            "enum_name": "CooperationMention",
            "enum_values": [
              "tak",
              "nie",
              "brak_wzmianki",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sprawca współpracował z organami ścigania, ujawnił współsprawców lub przekazał istotne informacje o przestępstwie. Typ: enum. Wymagalność: true.",
            "name": "cooperation_with_authorities"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd odnotował skruchę, żal lub krytyczny stosunek sprawcy do czynu. Typ: enum. Wymagalność: true.",
            "name": "remorse_expressed"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd zastosował lub wprost wskazał nadzwyczajne złagodzenie kary. Typ: enum. Wymagalność: true.",
            "name": "extraordinary_mitigation_applied"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd przyjął wypadek mniejszej wagi lub równoważny kwalifikator łagodzący w kwalifikacji prawnej czynu narkotykowego. Typ: enum. Wymagalność: true.",
            "name": "minor_case_applied"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: inne okoliczności łagodzące wskazane przez sąd, które nie mieszczą się w polach ustrukturyzowanych. Typ: string. Wymagalność: false.",
            "name": "additional_mitigating_circumstances"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: inne okoliczności obciążające wskazane przez sąd, które nie mieszczą się w polach ustrukturyzowanych. Typ: string. Wymagalność: false.",
            "name": "additional_aggravating_circumstances"
          },
          {
            "type_": "enum",
            "enum_name": "PrincipalPenalReaction",
            "enum_values": [
              "pozbawienie_wolnosci",
              "ograniczenie_wolnosci",
              "grzywna",
              "mieszana",
              "warunkowe_umorzenie",
              "warunkowe_przedterminowe_zwolnienie",
              "srodek_wychowawczy_lub_poprawczy",
              "inna_decyzja_wykonawcza",
              "inna",
              "nieustalone"
            ],
            "description": "Znaczenie: główny rodzaj finalnej reakcji karnej lub prawnokarnej zastosowanej wobec tego oskarżonego. Typ: enum. Wymagalność: true. Ekstrakcja: dla dokumentów wykonawczych używaj `warunkowe_przedterminowe_zwolnienie` albo `inna_decyzja_wykonawcza` zamiast ogólnego `inna`, gdy dokument realnie opisuje decyzję postpenalną.",
            "name": "principal_penal_reaction"
          },
          {
            "type_": "enum",
            "enum_name": "JuvenileReactionType",
            "enum_values": [
              "srodek_wychowawczy",
              "srodek_leczniczy",
              "srodek_poprawczy",
              "mieszane",
              "brak",
              "nieustalone"
            ],
            "description": "Znaczenie: znormalizowany typ reakcji stosowanej w postępowaniu wobec nieletniego; dla spraw w reżimie prawa karnego dorosłych zwykle użyj `brak`. Typ: enum. Wymagalność: true.",
            "name": "juvenile_reaction_type"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: opis środka lub środków zastosowanych wobec nieletniego w brzmieniu z orzeczenia. Typ: string. Wymagalność: false.",
            "name": "juvenile_reaction_text"
          },
          {
            "type_": "enum",
            "enum_name": "SentenceScope",
            "enum_values": [
              "reakcja_koncowa_wobec_oskarzonego",
              "kara_za_glowny_czyn_narkotykowy",
              "kara_laczna",
              "kara_w_sprawie_bazowej_opisana_posrednio",
              "nieustalone"
            ],
            "description": "Znaczenie: określa, do jakiego zakresu odnoszą się pola liczbowe o karze w tym rekordzie. Typ: enum. Wymagalność: true. Interpretuj łącznie z `sentence_relates_directly_to_drug_offense` i `drug_offense_sentence_identifiable`.",
            "name": "sentence_scope"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wymiar orzeczonej kary pozbawienia wolności w miesiącach zgodnie z zakresem określonym w `sentence_scope`, niezależnie od zawieszenia. Typ: integer. Wymagalność: false.",
            "name": "imprisonment_months"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wymiar orzeczonej kary ograniczenia wolności w miesiącach zgodnie z zakresem określonym w `sentence_scope`. Typ: integer. Wymagalność: false.",
            "name": "restriction_of_liberty_months"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: łączna kwota grzywny w złotych zgodnie z zakresem określonym w `sentence_scope`, jeśli da się ją ustalić. Typ: float. Wymagalność: false.",
            "name": "fine_total_pln"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: liczba stawek dziennych grzywny, jeśli grzywna została orzeczona w tej formie. Typ: integer. Wymagalność: false.",
            "name": "fine_daily_rates"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wysokość jednej stawki dziennej grzywny w złotych. Typ: float. Wymagalność: false.",
            "name": "fine_daily_rate_amount_pln"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wymiar kary pozbawienia wolności w miesiącach odnoszący się wyłącznie do czynu narkotykowego, jeśli da się go wyodrębnić. Typ: integer. Wymagalność: false. Wypełniaj tylko przy `drug_offense_sentence_identifiable = tak` lub `czesciowo`.",
            "name": "drug_offense_imprisonment_months"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: wymiar kary ograniczenia wolności w miesiącach odnoszący się wyłącznie do czynu narkotykowego, jeśli da się go wyodrębnić. Typ: integer. Wymagalność: false.",
            "name": "drug_offense_restriction_of_liberty_months"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: kwota grzywny w złotych odnosząca się wyłącznie do czynu narkotykowego, jeśli da się ją wyodrębnić. Typ: float. Wymagalność: false.",
            "name": "drug_offense_fine_total_pln"
          },
          {
            "type_": "enum",
            "enum_name": "SuspensionStatus",
            "enum_values": [
              "tak",
              "nie",
              "nie_dotyczy",
              "nieustalone"
            ],
            "description": "Znaczenie: czy wykonanie orzeczonej kary zostało warunkowo zawieszone wobec tego oskarżonego. Typ: enum. Wymagalność: true. Dla warunkowego umorzenia, środków wobec nieletnich lub decyzji czysto wykonawczych zwykle użyj `nie_dotyczy`.",
            "name": "sentence_conditionally_suspended"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: okres próby przy warunkowym zawieszeniu wykonania kary, wyrażony w miesiącach. Typ: integer. Wymagalność: false.",
            "name": "suspension_probation_period_months"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: okres próby przy warunkowym umorzeniu postępowania, wyrażony w miesiącach. Typ: integer. Wymagalność: false.",
            "name": "conditional_discontinuance_probation_months"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: przepisy dotyczące wymiaru kary, nadzwyczajnego złagodzenia, zawieszenia, warunkowego umorzenia lub innych środków probacyjnych wskazanych przez sąd. Typ: string. Wymagalność: false. Ekstrakcja: zapisuj jako listę przepisów rozdzieloną średnikami, np. `art. 53 k.k.; art. 69 § 1 k.k.; art. 70 § 1 k.k.`.",
            "name": "sentencing_provisions_text"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: podstawa prawna warunkowego zawieszenia wykonania kary wskazana przez sąd, jeśli została wyodrębniona w orzeczeniu. Typ: string. Wymagalność: false.",
            "name": "suspended_sentence_legal_basis_text"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: podstawa prawna warunkowego umorzenia postępowania wskazana przez sąd, jeśli została wyodrębniona w orzeczeniu. Typ: string. Wymagalność: false.",
            "name": "conditional_discontinuance_legal_basis_text"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd orzekł dozór w ramach zawieszenia, warunkowego umorzenia albo innego środka probacyjnego. Typ: enum. Wymagalność: true.",
            "name": "probation_supervision_imposed"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd orzekł obowiązek terapii, leczenia odwykowego, uczestnictwa w programie terapeutycznym lub podobny obowiązek związany z uzależnieniem. Typ: enum. Wymagalność: true.",
            "name": "therapy_or_addiction_treatment_obligation_imposed"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd orzekł świadczenie pieniężne, nawiązkę albo inny zbliżony obowiązek pieniężny niebędący grzywną. Typ: enum. Wymagalność: true.",
            "name": "pecuniary_payment_imposed"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd orzekł obowiązek naprawienia szkody, zadośćuczynienie lub podobny obowiązek kompensacyjny. Typ: enum. Wymagalność: true.",
            "name": "compensation_or_redress_imposed"
          },
          {
            "type_": "enum",
            "enum_name": "TriState",
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Znaczenie: czy sąd orzekł przepadek środków, korzyści, przedmiotów albo innych składników majątkowych związanych z czynem. Typ: enum. Wymagalność: true.",
            "name": "forfeiture_imposed"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: opis finansowych obowiązków lub rozstrzygnięć majątkowych towarzyszących reakcji karnej, wraz z kwotami lub przedmiotami, jeśli są podane. Typ: string. Wymagalność: false.",
            "name": "financial_obligations_text"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Znaczenie: inne obowiązki probacyjne lub środki towarzyszące, które mogą mieć znaczenie analityczne, np. zakazy, obowiązek informowania kuratora, powstrzymywanie się od używek. Typ: string. Wymagalność: false.",
            "name": "other_probation_obligations_text"
          }
        ]
        ```

=== "GPT-5.4 mini"

    **76 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `document_type` | enum | Type of document/ruling. Use `wyrok_laczny` only when the document deals exclusively with a combined sentence; `apelacja` for appellate rulings. |
        | `source_document_role` | enum | Role of the document in the study — distinguishes original judgment, appeal, and combined sentence. |
        | `source_record_scope` | enum | Scope of the document the record is drawn from — whole document, single defendant, single charge, single sentence, or mixed. |
        | `source_document_part` | enum | Main part of the document the record was drawn from. |
        | `age_information_source_part` | enum | Part of the document from which the defendant's age was determined. |
        | `sentence_information_source_part` | enum | Part of the document from which the sentence, its suspension, or conditional discontinuation was determined. |
        | `record_level` | enum | Level the record concerns — defendant, offense, sentence, or whole document. |
        | `document_relevance_to_narcotics_study` | enum | Usefulness of the document for studying the age-sentence relationship in drug cases. |
        | `narcotics_case_is_primary_subject` | boolean | Whether the drug case is the document's main subject. |
        | `case_outcome` | enum | Substantive outcome of the case for the defendant — mainly conviction or conditional discontinuation. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `document_type` | enum | Typ dokumentu/orzeczenia. Użyj `wyrok_laczny` tylko wtedy, gdy dokument dotyczy wyłącznie wyroku łącznego. `apelacja` stosuj, gdy dokumentem jest orzeczenie apelacyjne lub dokument o takim charakterze. |
        | `source_document_role` | enum | Rola dokumentu w badaniu. Użyj do odróżnienia wyroku pierwotnego, apelacji i wyroku łącznego; pole pomaga filtrować materiały nieporównywalne z orzeczeniami pierwszoinstancyjnymi. |
        | `source_record_scope` | enum | Zakres dokumentu, z którego pochodzi rekord. Użyj, aby zaznaczyć, czy dane dotyczą całego dokumentu, jednego oskarżonego, jednego czynu, jednej reakcji karnej czy materiału mieszanego. |
        | `source_document_part` | enum | Główna część dokumentu, z której pochodzi rekord. Wybierz część, w której faktycznie odnaleziono daną informację. |
        | `age_information_source_part` | enum | Część dokumentu, z której ustalono wiek oskarżonego. Szczególnie ważne, gdy wiek wynika z uzasadnienia, dat urodzenia albo dat czynu. |
        | `sentence_information_source_part` | enum | Część dokumentu, z której ustalono karę, zawieszenie wykonania kary albo warunkowe umorzenie postępowania. |
        | `record_level` | enum | Poziom, którego dotyczy rekord. Użyj `defendant` dla danych osoby, `offense` dla danych o czynie, `sentence` dla danych o reakcji karnej i `document` dla cech całego orzeczenia. |
        | `document_relevance_to_narcotics_study` | enum | Ocena przydatności dokumentu do badania zależności między wiekiem a karą w sprawach narkotykowych. Użyj `primary`, gdy dokument jest bezpośrednio o takim czynie, `secondary`, gdy jest tylko częściowo relewantny, `mixed`, gdy łączy kilka typów spraw, `not_relevant`, gdy nie nadaje się do analizy. |
        | `narcotics_case_is_primary_subject` | boolean | Czy sprawa narkotykowa jest głównym przedmiotem dokumentu. Ustaw `true`, gdy czyn narkotykowy stanowi centralny element orzeczenia; `false`, gdy pojawia się jedynie ubocznie. |
        | `case_outcome` | enum | Merytoryczny wynik sprawy wobec oskarżonego. Dla tej analizy używaj przede wszystkim `skazanie` albo `warunkowe_umorzenie`. |
    ??? note "Show full schema (76 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "enum",
            "enum_name": "document_type",
            "enum_values": [
              "wyrok_skazujacy",
              "warunkowe_umorzenie",
              "wyrok_laczny",
              "apelacja",
              "inne",
              "nieustalone"
            ],
            "description": "Typ dokumentu/orzeczenia. Użyj `wyrok_laczny` tylko wtedy, gdy dokument dotyczy wyłącznie wyroku łącznego. `apelacja` stosuj, gdy dokumentem jest orzeczenie apelacyjne lub dokument o takim charakterze.",
            "name": "document_type"
          },
          {
            "type_": "enum",
            "enum_name": "source_document_role",
            "enum_values": [
              "original_judgment",
              "appeal",
              "combined_sentence",
              "other",
              "nieustalone"
            ],
            "description": "Rola dokumentu w badaniu. Użyj do odróżnienia wyroku pierwotnego, apelacji i wyroku łącznego; pole pomaga filtrować materiały nieporównywalne z orzeczeniami pierwszoinstancyjnymi.",
            "name": "source_document_role"
          },
          {
            "type_": "enum",
            "enum_name": "source_record_scope",
            "enum_values": [
              "whole_document",
              "single_defendant",
              "single_charge",
              "single_sentence",
              "mixed",
              "nieustalone"
            ],
            "description": "Zakres dokumentu, z którego pochodzi rekord. Użyj, aby zaznaczyć, czy dane dotyczą całego dokumentu, jednego oskarżonego, jednego czynu, jednej reakcji karnej czy materiału mieszanego.",
            "name": "source_record_scope"
          },
          {
            "type_": "enum",
            "enum_name": "source_document_part",
            "enum_values": [
              "sentencja",
              "uzasadnienie",
              "apelacja",
              "postanowienie",
              "inne",
              "nieustalone"
            ],
            "description": "Główna część dokumentu, z której pochodzi rekord. Wybierz część, w której faktycznie odnaleziono daną informację.",
            "name": "source_document_part"
          },
          {
            "type_": "enum",
            "enum_name": "age_information_source_part",
            "enum_values": [
              "sentencja",
              "uzasadnienie",
              "apelacja",
              "postanowienie",
              "inne",
              "nieustalone"
            ],
            "description": "Część dokumentu, z której ustalono wiek oskarżonego. Szczególnie ważne, gdy wiek wynika z uzasadnienia, dat urodzenia albo dat czynu.",
            "name": "age_information_source_part"
          },
          {
            "type_": "enum",
            "enum_name": "sentence_information_source_part",
            "enum_values": [
              "sentencja",
              "uzasadnienie",
              "apelacja",
              "postanowienie",
              "inne",
              "nieustalone"
            ],
            "description": "Część dokumentu, z której ustalono karę, zawieszenie wykonania kary albo warunkowe umorzenie postępowania.",
            "name": "sentence_information_source_part"
          },
          {
            "type_": "enum",
            "enum_name": "record_level",
            "enum_values": [
              "document",
              "defendant",
              "offense",
              "sentence",
              "nieustalone"
            ],
            "description": "Poziom, którego dotyczy rekord. Użyj `defendant` dla danych osoby, `offense` dla danych o czynie, `sentence` dla danych o reakcji karnej i `document` dla cech całego orzeczenia.",
            "name": "record_level"
          },
          {
            "type_": "enum",
            "enum_name": "document_relevance_to_narcotics_study",
            "enum_values": [
              "primary",
              "secondary",
              "mixed",
              "not_relevant",
              "nieustalone"
            ],
            "description": "Ocena przydatności dokumentu do badania zależności między wiekiem a karą w sprawach narkotykowych. Użyj `primary`, gdy dokument jest bezpośrednio o takim czynie, `secondary`, gdy jest tylko częściowo relewantny, `mixed`, gdy łączy kilka typów spraw, `not_relevant`, gdy nie nadaje się do analizy.",
            "name": "document_relevance_to_narcotics_study"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sprawa narkotykowa jest głównym przedmiotem dokumentu. Ustaw `true`, gdy czyn narkotykowy stanowi centralny element orzeczenia; `false`, gdy pojawia się jedynie ubocznie.",
            "name": "narcotics_case_is_primary_subject"
          },
          {
            "type_": "enum",
            "enum_name": "case_outcome",
            "enum_values": [
              "skazanie",
              "warunkowe_umorzenie",
              "inne",
              "nieustalone"
            ],
            "description": "Merytoryczny wynik sprawy wobec oskarżonego. Dla tej analizy używaj przede wszystkim `skazanie` albo `warunkowe_umorzenie`.",
            "name": "case_outcome"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dokument jest wyrokiem łącznym. Ustaw `true` tylko wtedy, gdy sentencja dotyczy połączenia wcześniej orzeczonych kar.",
            "name": "is_combined_sentence"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w sprawie występują wcześniejsze wyroki lub skazania objęte wyrokiem łącznym. Pole stosuj wyłącznie przy `document_type=wyrok_laczny`.",
            "name": "underlying_judgments_present"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba wcześniejszych wyroków lub spraw objętych wyrokiem łącznym, jeśli dokument jest wyrokiem łącznym i da się to jednoznacznie ustalić.",
            "name": "underlying_judgment_count"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Oznaczenie oskarżonego, którego dotyczy rekord, np. inicjały, numer porządkowy albo inny identyfikator z dokumentu. Przydatne przy wielu oskarżonych.",
            "name": "defendant_identifier"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Oznaczenie czynu lub zarzutu, którego dotyczy rekord, np. numer czynu, punkt sentencji albo krótki opis. Przydatne przy wielu czynach w jednej sprawie.",
            "name": "charge_identifier"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy orzeczona kara lub decyzja procesowa dotyczy czynu narkotykowego, a nie wyłącznie innego równoległego czynu w tej samej sprawie.",
            "name": "sentence_targets_narcotics_offense"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Identyfikator czynu, do którego odnosi się orzeczona kara, zawieszenie albo warunkowe umorzenie. Użyj identyfikatora z `charge_identifier`; jeśli dotyczy kilku czynów, oddziel je średnikami.",
            "name": "sentence_target_charge_identifier"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba odrębnych czynów narkotykowych przypisanych temu oskarżonemu w dokumencie. Jeśli sprawa obejmuje kilka zarzutów narkotykowych, podaj liczbę możliwie jednoznacznie.",
            "name": "narcotics_offense_count"
          },
          {
            "type_": "enum",
            "enum_name": "narcotics_offense_main_type",
            "enum_values": [
              "posiadanie",
              "udzielanie",
              "obrót",
              "wprowadzanie_do_obrotu",
              "wytwarzanie",
              "przerabianie",
              "uprawa",
              "nabycie",
              "przemyt",
              "przechowywanie",
              "inne_narkotyczne",
              "nieustalone"
            ],
            "description": "Główny typ czynu narkotykowego przypisanego rekordowi. Jeśli w sprawie jest kilka czynów, wybierz typ najbardziej związany z wymiarem kary.",
            "name": "narcotics_offense_main_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy ten czyn narkotykowy jest czynem dominującym dla wymiaru kary w sprawie. Użyj szczególnie przy wielu zarzutach lub wieloczynowości.",
            "name": "narcotics_offense_is_primary_for_sentence"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Wszystkie typy czynów narkotykowych występujące w tym rekordzie, oddzielone średnikami. Użyj tego pola szczególnie w sprawach wieloczynowych.",
            "name": "narcotics_offense_types"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Pozostałe typy czynów narkotykowych występujące u tego oskarżonego; jeśli jest ich kilka, oddziel je średnikami.",
            "name": "narcotics_offense_additional_types"
          },
          {
            "type_": "enum",
            "enum_name": "offense_legal_basis_act",
            "enum_values": [
              "ustawa_o_przeciwdziałaniu_narkomanii",
              "kodeks_karny",
              "inne",
              "nieustalone"
            ],
            "description": "Akt prawny wskazany jako podstawa kwalifikacji czynu narkotykowego.",
            "name": "offense_legal_basis_act"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Artykuły, paragrafy i inne jednostki redakcyjne stanowiące podstawę kwalifikacji czynu narkotykowego; jeśli jest ich kilka, oddziel je średnikami.",
            "name": "offense_legal_basis_articles"
          },
          {
            "type_": "enum",
            "enum_name": "substance_category",
            "enum_values": [
              "środek_odurzający",
              "substancja_psychotropowa",
              "nowa_substancja_psychoaktywna",
              "mieszana",
              "nieustalone"
            ],
            "description": "Kategoria substancji objętej czynem, jeśli została wskazana w orzeczeniu.",
            "name": "substance_category"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Nazwa środka odurzającego, substancji psychotropowej lub nowej substancji psychoaktywnej; jeśli wskazano kilka substancji, oddziel je średnikami.",
            "name": "substance_name"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Ilość substancji wskazana w orzeczeniu jako wartość liczbowa, w jednostce podanej w `substance_quantity_unit`. Używaj tylko wtedy, gdy liczba jest jednoznaczna.",
            "name": "substance_quantity"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Tekstowy zapis ilości substancji, jeśli nie da się jej pewnie sprowadzić do jednej liczby, np. 'kilka gramów', 'około 10 porcji', 'znaczna ilość'.",
            "name": "substance_quantity_text"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy ilość substancji jest nieprecyzyjna, szacunkowa albo opisana bez jednoznacznej wartości liczbowej.",
            "name": "quantity_uncertain"
          },
          {
            "type_": "enum",
            "enum_name": "substance_quantity_unit",
            "enum_values": [
              "g",
              "mg",
              "kg",
              "ml",
              "tabletki",
              "porcje",
              "dawki",
              "sztuki",
              "opakowania",
              "inne",
              "nieustalone"
            ],
            "description": "Jednostka, w której podano ilość substancji; jeśli ilość jest opisana słownie lub wielkościowo, użyj `inne` albo `nieustalone`.",
            "name": "substance_quantity_unit"
          },
          {
            "type_": "enum",
            "enum_name": "substance_quantity_basis",
            "enum_values": [
              "netto",
              "brutto",
              "nieustalone"
            ],
            "description": "Podstawa podanej ilości substancji. Ustal, czy chodzi o ilość netto czy brutto; jeśli dokument tego nie rozróżnia, użyj `nieustalone`.",
            "name": "substance_quantity_basis"
          },
          {
            "type_": "enum",
            "enum_name": "purpose_of_action",
            "enum_values": [
              "na_wlasny_uzytek",
              "sprzedaż_lub_dalsza_odsprzedaż",
              "osiągnięcie_korzyści_majątkowej",
              "dystrybucja",
              "wprowadzenie_do_obrotu",
              "inne",
              "nieustalony"
            ],
            "description": "Ustalony lub wskazany w uzasadnieniu cel działania oskarżonego, np. na własny użytek, sprzedaż, dalsza odsprzedaż, wprowadzenie do obrotu, dystrybucja lub osiągnięcie korzyści majątkowej.",
            "name": "purpose_of_action"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Dodatkowy opis celu działania, jeśli cel nie mieści się w wartościach enuma albo wymaga doprecyzowania. Zachowaj możliwie wierne brzmienie z dokumentu.",
            "name": "purpose_of_action_description"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy z dokumentu można wiarygodnie ustalić wiek oskarżonego w chwili czynu lub orzekania.",
            "name": "age_data_available"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Krótki powód, dla którego wieku nie dało się wyliczyć lub ustalić. Użyj, gdy brak dat, podano tylko zakres, albo dane są sprzeczne.",
            "name": "age_not_derived_reason"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Data urodzenia oskarżonego, najlepiej w formacie YYYY-MM-DD; jeśli dokument podaje tylko rok albo inny zakres, zachowaj zapis tekstowy.",
            "name": "date_of_birth"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Data popełnienia czynu lub zakres dat czynu, jeśli taki zakres podano w dokumentach. Pole służy do wyliczania wieku w chwili czynu.",
            "name": "offense_date"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Dokładny wiek oskarżonego w chwili popełnienia czynu, jeśli można go wiarygodnie wyliczyć z daty urodzenia i daty czynu albo jeśli wiek podano wprost.",
            "name": "age_at_offense_years"
          },
          {
            "type_": "enum",
            "enum_name": "age_at_offense_bracket_5",
            "enum_values": [
              "poniżej_18",
              "18_20",
              "21_24",
              "25_34",
              "35_plus"
            ],
            "description": "Pięcioklasowy przedział wieku oskarżonego w chwili czynu. Stosuj stałe granice analityczne: poniżej 18 lat, 18–20, 21–24, 25–34, 35+.",
            "name": "age_at_offense_bracket_5"
          },
          {
            "type_": "enum",
            "enum_name": "age_status_at_offense",
            "enum_values": [
              "nieletni",
              "młodociany",
              "dorosły",
              "nieustalony"
            ],
            "description": "Status wieku oskarżonego w chwili popełnienia czynu. Użyj kategorii wynikającej z treści dokumentu i przepisów; nie myl jej z samym wiekiem liczbowym.",
            "name": "age_status_at_offense"
          },
          {
            "type_": "enum",
            "enum_name": "offense_age_source",
            "enum_values": [
              "wprost_podany",
              "wyliczony",
              "przyblizony",
              "nieustalony"
            ],
            "description": "Źródło informacji o wieku w chwili czynu. Użyj `wprost_podany`, gdy wiek jest zapisany wprost; `wyliczony`, gdy wynika z dat; `przyblizony`, gdy podano zakres lub opis przybliżony; `nieustalony`, gdy brak pewności.",
            "name": "offense_age_source"
          },
          {
            "type_": "enum",
            "enum_name": "offense_age_confidence",
            "enum_values": [
              "wysoka",
              "srednia",
              "niska",
              "nieustalona"
            ],
            "description": "Ocena pewności ekstrakcji wieku w chwili czynu na podstawie treści dokumentu i możliwości jednoznacznego ustalenia dat.",
            "name": "offense_age_confidence"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Dokładny wiek oskarżonego w chwili orzekania w pierwszej instancji, jeśli można go wiarygodnie wyliczyć lub jeśli podano go wprost.",
            "name": "age_at_judgment_years"
          },
          {
            "type_": "enum",
            "enum_name": "age_at_judgment_bracket_5",
            "enum_values": [
              "poniżej_18",
              "18_20",
              "21_24",
              "25_34",
              "35_plus"
            ],
            "description": "Pięcioklasowy przedział wieku oskarżonego w chwili orzekania; stosuj te same granice co dla wieku w chwili czynu.",
            "name": "age_at_judgment_bracket_5"
          },
          {
            "type_": "enum",
            "enum_name": "age_status_at_judgment",
            "enum_values": [
              "nieletni",
              "młodociany",
              "dorosły",
              "nieustalony"
            ],
            "description": "Status wieku oskarżonego w chwili orzekania. Przydatne zwłaszcza wtedy, gdy dokument podaje daty pozwalające odróżnić wiek w chwili czynu i w chwili wyroku.",
            "name": "age_status_at_judgment"
          },
          {
            "type_": "enum",
            "enum_name": "judgment_age_source",
            "enum_values": [
              "wprost_podany",
              "wyliczony",
              "przyblizony",
              "nieustalony"
            ],
            "description": "Źródło informacji o wieku w chwili orzekania. Użyj tych samych zasad co dla wieku w chwili czynu.",
            "name": "judgment_age_source"
          },
          {
            "type_": "enum",
            "enum_name": "judgment_age_confidence",
            "enum_values": [
              "wysoka",
              "srednia",
              "niska",
              "nieustalona"
            ],
            "description": "Ocena pewności ekstrakcji wieku w chwili orzekania.",
            "name": "judgment_age_confidence"
          },
          {
            "type_": "enum",
            "enum_name": "sentence_main_type",
            "enum_values": [
              "pozbawienie_wolności",
              "grzywna",
              "ograniczenie_wolności",
              "kara_łączona",
              "brak",
              "inna",
              "nieustalony"
            ],
            "description": "Główny rodzaj reakcji karnej orzeczonej wobec oskarżonego. Przy warunkowym umorzeniu użyj `brak`.",
            "name": "sentence_main_type"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wymiar kary pozbawienia wolności w miesiącach, jeśli została orzeczona. Jeżeli kara podana jest w latach i miesiącach, przelicz ją na miesiące.",
            "name": "imprisonment_months"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wykonanie orzeczonej kary pozbawienia wolności zostało warunkowo zawieszone.",
            "name": "imprisonment_suspended"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Okres próby przy warunkowym zawieszeniu wykonania kary pozbawienia wolności, w miesiącach.",
            "name": "suspension_period_months"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Opis obowiązków, środków probacyjnych lub warunków związanych z zawieszeniem kary albo warunkowym umorzeniem postępowania.",
            "name": "probation_obligations_description"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy zastosowano warunkowe umorzenie postępowania wobec tego oskarżonego.",
            "name": "conditional_discontinuance_present"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Okres próby przy warunkowym umorzeniu postępowania, w miesiącach.",
            "name": "conditional_discontinuance_period_months"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba stawek dziennych grzywny, jeśli grzywnę orzeczono w takiej postaci.",
            "name": "fine_daily_rates"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wysokość jednej stawki dziennej grzywny w złotych, jeśli została wskazana.",
            "name": "fine_daily_rate_amount_pln"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Łączna wysokość orzeczonej grzywny w złotych.",
            "name": "fine_amount_pln"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wymiar kary ograniczenia wolności w miesiącach, jeśli została orzeczona.",
            "name": "restriction_of_liberty_months"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba godzin pracy społecznej lub innego obowiązku w ramach ograniczenia wolności, jeśli została wskazana.",
            "name": "restriction_of_liberty_hours_per_month"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Dodatkowe sankcje, środki karne, przepadek, świadczenia pieniężne lub inne elementy reakcji karnej, które wpływają na ocenę surowości, a nie zostały ujęte osobno.",
            "name": "additional_sanctions_description"
          },
          {
            "type_": "enum",
            "enum_name": "sentence_legal_basis_act",
            "enum_values": [
              "kodeks_karny",
              "ustawa_o_przeciwdziałaniu_narkomanii",
              "inne",
              "nieustalone"
            ],
            "description": "Akt prawny wskazany jako podstawa rozstrzygnięcia o karze, zawieszeniu wykonania kary albo warunkowym umorzeniu.",
            "name": "sentence_legal_basis_act"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Artykuły i paragrafy stanowiące ogólną podstawę wymiaru kary; jeśli jest ich kilka, oddziel je średnikami. Nie używaj tego pola do szczegółowej podstawy zawieszenia lub umorzenia, jeśli można je wydzielić osobno.",
            "name": "sentence_basis_articles"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Artykuły i paragrafy stanowiące podstawę warunkowego zawieszenia wykonania kary; jeśli występują, wyodrębnij je z sentencji lub uzasadnienia.",
            "name": "suspension_basis_articles"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Artykuły i paragrafy stanowiące podstawę warunkowego umorzenia postępowania; jeśli występują, wyodrębnij je z sentencji lub uzasadnienia.",
            "name": "conditional_discontinuance_basis_articles"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w orzeczeniu wskazano uprzednią karalność oskarżonego.",
            "name": "prior_conviction_present"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w sprawie stwierdzono recydywę.",
            "name": "recidivism_present"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy oskarżony był uzależniony od środków odurzających lub substancji psychotropowych.",
            "name": "addiction_present"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy działanie miało na celu osiągnięcie korzyści majątkowej.",
            "name": "profit_motive_present"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy czyn został popełniony wspólnie z inną osobą lub innymi osobami.",
            "name": "cooffending_present"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Konkretnie wskazane okoliczności łagodzące w sprawie; jeśli jest ich kilka, oddziel je średnikami.",
            "name": "mitigating_circumstances_list"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Konkretnie wskazane okoliczności obciążające w sprawie; jeśli jest ich kilka, oddziel je średnikami.",
            "name": "aggravating_circumstances_list"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wobec tego oskarżonego występowały inne, równoległe czyny zabronione rozpoznawane w tej samej sprawie. Nie używaj tego pola dla wyroku łącznego ani dla wcześniejszych wyroków.",
            "name": "defendant_parallel_offenses_present"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba równoległych czynów zabronionych uwzględnionych wobec tego oskarżonego w tej samej sprawie, jeśli da się ją ustalić.",
            "name": "defendant_parallel_offenses_count"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Rodzaje równoległych czynów zabronionych występujących wobec tego oskarżonego; jeśli jest ich kilka, oddziel je średnikami.",
            "name": "defendant_parallel_offense_types"
          },
          {
            "type_": "enum",
            "enum_name": "defendant_parallel_offense_legal_basis_act",
            "enum_values": [
              "ustawa_o_przeciwdziałaniu_narkomanii",
              "kodeks_karny",
              "inne",
              "nieustalone"
            ],
            "description": "Akt prawny wskazany jako podstawa równoległych czynów zabronionych, jeśli został wymieniony.",
            "name": "defendant_parallel_offense_legal_basis_act"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Artykuły, paragrafy i inne jednostki redakcyjne dotyczące równoległych czynów zabronionych wobec tego oskarżonego; jeśli jest ich kilka, oddziel je średnikami.",
            "name": "defendant_parallel_offense_legal_basis_articles"
          }
        ]
        ```

=== "Claude Sonnet 4.6"

    **68 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `has_full_reasoning` | enum | Type of reasoning available in the document — full first-instance reasoning, abbreviated, appellate reasoning without its own sentencing rationale, appellate reasoning with its own sentencing rationale, or no reasoning at all. |
        | `defendant_age_data_available` | boolean | Whether any information on the defendant's age was available in the document (birth date, stated age, ID number, or a computable age). |
        | `verdict_type` | enum | Type of ruling — conviction or conditional discontinuation (Art. 66-67 Penal Code). Acquittals are excluded from the analysis. |
        | `court_instance` | enum | Instance of the court that issued the ruling — first instance or appellate. |
        | `remand_after_cassation` | boolean | Whether the case was remanded for retrial after a Supreme Court cassation or an appellate court's reversal. |
        | `defendant_age_at_offense` | integer | Defendant's age in full years at the time of the offense. |
        | `defendant_age_at_ruling` | integer | Defendant's age in full years at the time of the first-instance ruling. |
        | `defendant_gender` | enum | Defendant's gender, used as a statistical control variable. |
        | `defendant_is_young_adult` | boolean | Whether the court recognized the defendant as a "young adult" under Art. 115 §10 of the Penal Code. |
        | `multiple_defendants_in_case` | boolean | Whether the same case involves other co-defendants besides the one this record concerns. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `has_full_reasoning` | enum | Typ uzasadnienia dostępnego w dokumencie. 'uzasadnienie_I_instancji_pelne' — pełne uzasadnienie faktyczne i prawne sądu I instancji; 'uzasadnienie_I_instancji_skrocone' — uzasadnienie skrócone lub częściowe sądu I instancji; 'uzasadnienie_odwolawcze' — uzasadnienie sądu II instancji ograniczone do kontroli procesowej, bez własnego merytorycznego uzasadnienia wymiaru kary; 'uzasadnienie_odwolawcze_z_wlasnym_wymiarem_kary' — uzasadnienie sądu II instancji, w którym sąd apelacyjny lub okręgowy samodzielnie wymierzył karę i zawarł własne merytoryczne rozważania o jej wymiarze (np. po uchyleniu i zmianie wyroku I instancji) — ta wartość NIE zeruje pól mitigating_*/aggravating_*/recidivism_type/addiction_treated_as_mitigating/art_54_kk_applied; 'brak_uzasadnienia' — dokument zawiera wyłącznie sentencję lub protokół bez uzasadnienia. Sentinel: gdy wartość to 'uzasadnienie_odwolawcze' lub 'brak_uzasadnienia', pola mitigating_*, aggravating_*, recidivism_type, addiction_treated_as_mitigating, art_54_kk_applied powinny mieć wartość null z powodu braku danych. |
        | `defendant_age_data_available` | boolean | Czy dane o wieku oskarżonego były dostępne w dokumencie w jakiejkolwiek formie (data urodzenia, wiek wprost podany, PESEL, wiek możliwy do obliczenia). False gdy data urodzenia jest w całości zanonimizowana jako '(...)' lub brak jakiejkolwiek wzmianki o wieku — wówczas pola defendant_age_at_offense i defendant_age_at_ruling będą null z powodu braku danych. UWAGA: jeśli w dokumencie pojawia się wiek wyłącznie w kontekście ofiary/nabywcy (np. małoletni nabywca), a nie oskarżonego, wartość tego pola to false — wiek ofiary nie jest wiekiem oskarżonego. |
        | `verdict_type` | enum | Rodzaj orzeczenia: wyrok skazujący lub warunkowe umorzenie postępowania (art. 66–67 k.k.). Orzeczenia uniewinniające są wykluczone z analizy i nie powinny być ekstrahowane. |
        | `court_instance` | enum | Instancja sądu wydającego orzeczenie: pierwsza (sąd rejonowy lub okręgowy jako I instancja) lub odwoławcza (sąd okręgowy lub apelacyjny jako II instancja). Umożliwia filtrowanie wyroków I instancji na potrzeby analizy statusu młodocianego. |
        | `remand_after_cassation` | boolean | Czy sprawa wróciła do ponownego rozpoznania lub zmiany po kasacji Sądu Najwyższego lub po uchyleniu wyroku przez sąd apelacyjny. True gdy dokument lub jego kontekst wskazuje, że wyrok jest efektem ponownego rozpoznania po kasacji/uchyleniu. Istotne dla interpretacji surowości kary w kontekście zakazu reformationis in peius (art. 434 k.p.k.) oraz porównywalności z wyrokami pierwotnymi. False gdy brak wzmianki o wcześniejszym uchyleniu. |
        | `defendant_age_at_offense` | integer | Wiek oskarżonego w chwili popełnienia czynu (w latach pełnych). Wartość numeryczna do analiz ilościowych i regresji. Gdy data urodzenia jest zanonimizowana, oszacować jako: defendant_age_at_ruling minus liczba lat między datą czynu a datą wyroku — pole może być wówczas przybliżone o ±1 rok. UWAGA: nie używać wieku ofiary (np. małoletniego nabywcy narkotyków) jako proxy — jeśli wiek pojawia się wyłącznie w kontekście ofiary, przypisać null i ustawić defendant_age_data_available = false. Null gdy brak jakichkolwiek danych pozwalających na obliczenie lub oszacowanie. |
        | `defendant_age_at_ruling` | integer | Wiek oskarżonego w chwili wydania wyroku w I instancji (w latach pełnych). Niezbędne do algorytmicznej weryfikacji statusu młodocianego z art. 115 §10 k.k. UWAGA: nie używać wieku ofiary (np. małoletniego nabywcy narkotyków) jako proxy — jeśli wiek pojawia się wyłącznie w kontekście ofiary, przypisać null. Null gdy brak informacji w dokumencie — zob. pole defendant_age_data_available. |
        | `defendant_gender` | enum | Płeć oskarżonego jako zmienna kontrolna w analizie statystycznej. Wartość 'nieustalona' gdy dokument nie zawiera wyraźnej informacji o płci. |
        | `defendant_is_young_adult` | boolean | Czy sąd uznał oskarżonego za młodocianego w rozumieniu art. 115 §10 k.k. (nie ukończył 21 lat w chwili czynu i 24 lat w chwili orzekania w I instancji), co skutkuje zastosowaniem dyrektyw z art. 54 k.k. przy wymiarze kary. True tylko gdy sąd explicite powołuje ten status. Null gdy defendant_age_data_available = false. |
        | `multiple_defendants_in_case` | boolean | Czy w tej samej sprawie sądowej oprócz oskarżonego, którego dotyczy ten rekord, występują inni współoskarżeni. True sygnalizuje ryzyko mieszania danych różnych oskarżonych przy ekstrakcji automatycznej — dane ilościowe (ilość narkotyków, wymiar kary) powinny być przypisywane wyłącznie oskarżonemu będącemu jednostką analizy w tym rekordzie, nie współoskarżonym. |
    ??? note "Show full schema (68 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "enum",
            "enum_name": "ReasoningType",
            "enum_values": [
              "uzasadnienie_I_instancji_pelne",
              "uzasadnienie_I_instancji_skrocone",
              "uzasadnienie_odwolawcze",
              "uzasadnienie_odwolawcze_z_wlasnym_wymiarem_kary",
              "brak_uzasadnienia"
            ],
            "description": "Typ uzasadnienia dostępnego w dokumencie. 'uzasadnienie_I_instancji_pelne' — pełne uzasadnienie faktyczne i prawne sądu I instancji; 'uzasadnienie_I_instancji_skrocone' — uzasadnienie skrócone lub częściowe sądu I instancji; 'uzasadnienie_odwolawcze' — uzasadnienie sądu II instancji ograniczone do kontroli procesowej, bez własnego merytorycznego uzasadnienia wymiaru kary; 'uzasadnienie_odwolawcze_z_wlasnym_wymiarem_kary' — uzasadnienie sądu II instancji, w którym sąd apelacyjny lub okręgowy samodzielnie wymierzył karę i zawarł własne merytoryczne rozważania o jej wymiarze (np. po uchyleniu i zmianie wyroku I instancji) — ta wartość NIE zeruje pól mitigating_*/aggravating_*/recidivism_type/addiction_treated_as_mitigating/art_54_kk_applied; 'brak_uzasadnienia' — dokument zawiera wyłącznie sentencję lub protokół bez uzasadnienia. Sentinel: gdy wartość to 'uzasadnienie_odwolawcze' lub 'brak_uzasadnienia', pola mitigating_*, aggravating_*, recidivism_type, addiction_treated_as_mitigating, art_54_kk_applied powinny mieć wartość null z powodu braku danych.",
            "name": "has_full_reasoning"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dane o wieku oskarżonego były dostępne w dokumencie w jakiejkolwiek formie (data urodzenia, wiek wprost podany, PESEL, wiek możliwy do obliczenia). False gdy data urodzenia jest w całości zanonimizowana jako '(...)' lub brak jakiejkolwiek wzmianki o wieku — wówczas pola defendant_age_at_offense i defendant_age_at_ruling będą null z powodu braku danych. UWAGA: jeśli w dokumencie pojawia się wiek wyłącznie w kontekście ofiary/nabywcy (np. małoletni nabywca), a nie oskarżonego, wartość tego pola to false — wiek ofiary nie jest wiekiem oskarżonego.",
            "name": "defendant_age_data_available"
          },
          {
            "type_": "enum",
            "enum_name": "VerdictType",
            "enum_values": [
              "wyrok_skazujacy",
              "warunkowe_umorzenie"
            ],
            "description": "Rodzaj orzeczenia: wyrok skazujący lub warunkowe umorzenie postępowania (art. 66–67 k.k.). Orzeczenia uniewinniające są wykluczone z analizy i nie powinny być ekstrahowane.",
            "name": "verdict_type"
          },
          {
            "type_": "enum",
            "enum_name": "CourtInstance",
            "enum_values": [
              "pierwsza",
              "odwolawcza"
            ],
            "description": "Instancja sądu wydającego orzeczenie: pierwsza (sąd rejonowy lub okręgowy jako I instancja) lub odwoławcza (sąd okręgowy lub apelacyjny jako II instancja). Umożliwia filtrowanie wyroków I instancji na potrzeby analizy statusu młodocianego.",
            "name": "court_instance"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sprawa wróciła do ponownego rozpoznania lub zmiany po kasacji Sądu Najwyższego lub po uchyleniu wyroku przez sąd apelacyjny. True gdy dokument lub jego kontekst wskazuje, że wyrok jest efektem ponownego rozpoznania po kasacji/uchyleniu. Istotne dla interpretacji surowości kary w kontekście zakazu reformationis in peius (art. 434 k.p.k.) oraz porównywalności z wyrokami pierwotnymi. False gdy brak wzmianki o wcześniejszym uchyleniu.",
            "name": "remand_after_cassation"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wiek oskarżonego w chwili popełnienia czynu (w latach pełnych). Wartość numeryczna do analiz ilościowych i regresji. Gdy data urodzenia jest zanonimizowana, oszacować jako: defendant_age_at_ruling minus liczba lat między datą czynu a datą wyroku — pole może być wówczas przybliżone o ±1 rok. UWAGA: nie używać wieku ofiary (np. małoletniego nabywcy narkotyków) jako proxy — jeśli wiek pojawia się wyłącznie w kontekście ofiary, przypisać null i ustawić defendant_age_data_available = false. Null gdy brak jakichkolwiek danych pozwalających na obliczenie lub oszacowanie.",
            "name": "defendant_age_at_offense"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wiek oskarżonego w chwili wydania wyroku w I instancji (w latach pełnych). Niezbędne do algorytmicznej weryfikacji statusu młodocianego z art. 115 §10 k.k. UWAGA: nie używać wieku ofiary (np. małoletniego nabywcy narkotyków) jako proxy — jeśli wiek pojawia się wyłącznie w kontekście ofiary, przypisać null. Null gdy brak informacji w dokumencie — zob. pole defendant_age_data_available.",
            "name": "defendant_age_at_ruling"
          },
          {
            "type_": "enum",
            "enum_name": "DefendantGender",
            "enum_values": [
              "mezczyzna",
              "kobieta",
              "nieustalona"
            ],
            "description": "Płeć oskarżonego jako zmienna kontrolna w analizie statystycznej. Wartość 'nieustalona' gdy dokument nie zawiera wyraźnej informacji o płci.",
            "name": "defendant_gender"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd uznał oskarżonego za młodocianego w rozumieniu art. 115 §10 k.k. (nie ukończył 21 lat w chwili czynu i 24 lat w chwili orzekania w I instancji), co skutkuje zastosowaniem dyrektyw z art. 54 k.k. przy wymiarze kary. True tylko gdy sąd explicite powołuje ten status. Null gdy defendant_age_data_available = false.",
            "name": "defendant_is_young_adult"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w tej samej sprawie sądowej oprócz oskarżonego, którego dotyczy ten rekord, występują inni współoskarżeni. True sygnalizuje ryzyko mieszania danych różnych oskarżonych przy ekstrakcji automatycznej — dane ilościowe (ilość narkotyków, wymiar kary) powinny być przypisywane wyłącznie oskarżonemu będącemu jednostką analizy w tym rekordzie, nie współoskarżonym.",
            "name": "multiple_defendants_in_case"
          },
          {
            "type_": "enum",
            "enum_name": "OffenseType",
            "enum_values": [
              "posiadanie",
              "obrot_udzielanie",
              "obrot_wprowadzanie",
              "wytwarzanie_przetwarzanie",
              "inne_narkotykowe"
            ],
            "description": "Główny typ przestępstwa narkotykowego przypisanego oskarżonemu: posiadanie (art. 62 u.p.n.), udzielanie (art. 58–59 u.p.n.), wprowadzanie do obrotu (art. 56 u.p.n.), wytwarzanie lub przetwarzanie (art. 53 u.p.n.) lub inne przestępstwo z ustawy o przeciwdziałaniu narkomanii (np. przemyt art. 55, uprawa art. 63).",
            "name": "primary_offense_type"
          },
          {
            "type_": "enum",
            "enum_name": "OffenseForm",
            "enum_values": [
              "sprawstwo",
              "wspolsprawstwo",
              "pomocnictwo",
              "podzelganie",
              "nieustalona"
            ],
            "description": "Forma zjawiskowa czynu przypisana oskarżonemu przez sąd: sprawstwo (art. 18 §1 k.k., w tym sprawstwo kierownicze i polecające), współsprawstwo (art. 18 §1 k.k. in fine), pomocnictwo (art. 18 §3 k.k.), podżeganie (art. 18 §2 k.k.), nieustalona gdy dokument nie pozwala na jednoznaczne określenie. Kluczowe dla interpretacji wymiaru kary — pomocnictwo i podżeganie skutkują istotnie innymi ramami zagrożenia niż sprawstwo. Szukać w opisie czynu w sentencji lub w kwalifikacji prawnej (np. 'w zw. z art. 18 §3 k.k.').",
            "name": "offense_form"
          },
          {
            "type_": "enum",
            "enum_name": "LegalBasis",
            "enum_values": [
              "art_53_upn",
              "art_55_upn",
              "art_56_upn",
              "art_57_upn",
              "art_58_upn",
              "art_59_upn",
              "art_62_upn",
              "art_63_upn",
              "inne_upn"
            ],
            "description": "Podstawa prawna głównego zarzutu narkotykowego z ustawy o przeciwdziałaniu narkomanii (u.p.n.): art. 53 (wytwarzanie), art. 55 (przemyt), art. 56 (obrót), art. 57 (nakłanianie), art. 58 (udzielanie nieodpłatne), art. 59 (udzielanie odpłatne), art. 62 (posiadanie), art. 63 (uprawa). W przypadku wielu zarzutów wskazać artykuł odnoszący się do najpoważniejszego czynu. Wartość 'inne_upn' dla pozostałych artykułów ustawy.",
            "name": "legal_basis_article"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Ustęp (ust.) głównego przepisu u.p.n. wskazany w podstawie prawnej, np. 'ust. 1', 'ust. 2', 'ust. 3'. Uzupełnia pole legal_basis_article — umożliwia rozróżnienie typów podstawowych, kwalifikowanych i wypadku mniejszej wagi bez konieczności łączenia z offense_minor_case. Przykłady: art. 62 ust. 1 (typ podstawowy posiadania), art. 62 ust. 2 (typ kwalifikowany — znaczna ilość), art. 62 ust. 3 (wypadek mniejszej wagi); art. 58 ust. 1 (udzielanie), art. 58 ust. 2 (udzielanie małoletniemu). Null gdy ustęp nie jest wskazany w dokumencie lub nie daje się ustalić.",
            "name": "legal_basis_paragraph"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Drugi artykuł podstawy prawnej przy kumulatywnej kwalifikacji z art. 11 §2 k.k. (np. 'art. 63 ust. 3 u.p.n.' gdy czyn zakwalifikowano kumulatywnie jako art. 63 ust. 3 + art. 53 ust. 2 u.p.n.). Podawać jako tekst, np. 'art. 63 ust. 3 u.p.n.' lub 'art. 53 ust. 2 u.p.n.'. Null jeśli brak kumulatywnej kwalifikacji lub tylko jeden artykuł u.p.n.",
            "name": "legal_basis_secondary_article"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy czyn zakwalifikowano jako wypadek mniejszej wagi w rozumieniu właściwego przepisu ustawy o przeciwdziałaniu narkomanii (np. art. 62 ust. 3, art. 59 ust. 3 u.p.n.) — kwalifikacja istotnie obniżająca ustawowe zagrożenie karą.",
            "name": "offense_minor_case"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sprawa obejmuje więcej niż jeden artykuł ustawy o przeciwdziałaniu narkomanii przypisany oskarżonemu (np. jednocześnie posiadanie z art. 62 i udzielanie z art. 59 u.p.n.).",
            "name": "multiple_drug_charges"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy ofiara lub odbiorca środka odurzającego/substancji psychotropowej była osobą małoletnią — przesłanka kwalifikująca czyn z art. 58 ust. 2 lub art. 59 ust. 2 u.p.n. (udzielanie/sprzedaż małoletniemu). True gdy sąd stwierdza małoletniość ofiary w opisie czynu lub uzasadnieniu. False gdy brak małoletniego odbiorcy lub nierelewantne (np. posiadanie, wytwarzanie bez udzielania). Null gdy nie można ustalić z treści dokumentu.",
            "name": "victim_is_minor"
          },
          {
            "type_": "enum",
            "enum_name": "DrugSubstance",
            "enum_values": [
              "marihuana_konopie",
              "amfetamina",
              "metamfetamina",
              "kokaina",
              "heroina",
              "mdma_ekstazy",
              "inne",
              "wiele_substancji"
            ],
            "description": "Główny rodzaj zabezpieczonego środka odurzającego lub substancji psychotropowej wymienionej w orzeczeniu. Przy wielu różnych substancjach wybrać 'wiele_substancji'. Wartość 'inne' dla substancji spoza listy (np. fentanyl, GHB).",
            "name": "drug_substance_type"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Ilość głównego (pierwszego) środka odurzającego lub substancji psychotropowej USTALONA PRZEZ SĄD W WYROKU (nie zarzucana w akcie oskarżenia), wyrażona w jednostce wskazanej w polu drug_quantity_unit. Kryterium wyboru 'głównej substancji': substancja o największej masie (w gramach) spośród wszystkich zabezpieczonych; przy braku możliwości porównania mas (np. różne jednostki niemierzalne) — pierwsza wymieniona w sentencji wyroku. W przypadku rozbieżności między zarzutem a ustaleniem sądowym — podawać wartość z ustaleń sądu. Ilość zarzucaną rejestruje osobno pole drug_quantity_as_charged. Null jeśli sąd nie ustalił ilości w wyroku.",
            "name": "drug_quantity_value"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Ilość głównego środka odurzającego ZARZUCANA W AKCIE OSKARŻENIA (nie ustalona przez sąd), wyrażona w tej samej jednostce co drug_quantity_unit. Wypełniać wyłącznie gdy w dokumencie jest wyraźna rozbieżność między ilością zarzucaną a ustaloną przez sąd. Null gdy brak rozbieżności lub gdy akt oskarżenia nie podaje ilości.",
            "name": "drug_quantity_as_charged"
          },
          {
            "type_": "enum",
            "enum_name": "DrugQuantityUnit",
            "enum_values": [
              "gramy",
              "kilogramy",
              "mililitry",
              "sztuki_tabletki",
              "dzialki_porcje",
              "inne"
            ],
            "description": "Jednostka miary ilości głównego środka odurzającego podana w orzeczeniu. Uzupełnienie pola drug_quantity_value. Wartość 'inne' gdy jednostka jest niestandardowa lub niejasna. Null jeśli drug_quantity_value jest null.",
            "name": "drug_quantity_unit"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Ilość drugiego zabezpieczonego środka odurzającego przy sprawach wielosubstancyjnych (drug_substance_type = 'wiele_substancji'), wyrażona w jednostce wskazanej w polu drug_quantity_unit_2. Null jeśli sprawa dotyczy tylko jednej substancji lub ilości nie podano.",
            "name": "drug_quantity_value_2"
          },
          {
            "type_": "enum",
            "enum_name": "DrugQuantityUnit",
            "enum_values": [
              "gramy",
              "kilogramy",
              "mililitry",
              "sztuki_tabletki",
              "dzialki_porcje",
              "inne"
            ],
            "description": "Jednostka miary ilości drugiego środka odurzającego przy sprawach wielosubstancyjnych. Uzupełnienie pola drug_quantity_value_2. Null jeśli drug_quantity_value_2 jest null.",
            "name": "drug_quantity_unit_2"
          },
          {
            "type_": "float",
            "enum_name": null,
            "enum_values": [],
            "description": "Ilość trzeciego zabezpieczonego środka odurzającego przy sprawach wielosubstancyjnych obejmujących co najmniej trzy substancje (drug_substance_type = 'wiele_substancji'), wyrażona w jednostce wskazanej w polu drug_quantity_unit_3. Null jeśli sprawa dotyczy mniej niż trzech substancji lub ilości nie podano.",
            "name": "drug_quantity_value_3"
          },
          {
            "type_": "enum",
            "enum_name": "DrugQuantityUnit",
            "enum_values": [
              "gramy",
              "kilogramy",
              "mililitry",
              "sztuki_tabletki",
              "dzialki_porcje",
              "inne"
            ],
            "description": "Jednostka miary ilości trzeciego środka odurzającego przy sprawach wielosubstancyjnych. Uzupełnienie pola drug_quantity_value_3. Null jeśli drug_quantity_value_3 jest null.",
            "name": "drug_quantity_unit_3"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy ilość zabezpieczonego środka została przez sąd wprost zakwalifikowana jako 'znaczna' — pojęcie ustawowe wpływające na kwalifikację z typu kwalifikowanego (np. art. 62 ust. 2, art. 56 ust. 3 u.p.n.) i wymiar kary.",
            "name": "drug_quantity_significant"
          },
          {
            "type_": "enum",
            "enum_name": "PossessionPurpose",
            "enum_values": [
              "wlasny_uzyt",
              "obrot_udzielanie",
              "nieustalony",
              "nie_dotyczy_wytwarzanie"
            ],
            "description": "Cel posiadania środka odurzającego ustalony przez sąd: wyłącznie na własny użytek, w celu wprowadzenia do obrotu lub udzielenia innej osobie, lub nieustalony przez sąd. Wartość 'nie_dotyczy_wytwarzanie' stosować gdy główny czyn to wytwarzanie (art. 53 u.p.n.) lub uprawa (art. 63 u.p.n.) i cel posiadania nie jest formalnym znamieniem czynu. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'] i sąd nie wskazał celu w sentencji.",
            "name": "possession_purpose"
          },
          {
            "type_": "enum",
            "enum_name": "SentenceType",
            "enum_values": [
              "pozbawienie_wolnosci",
              "ograniczenie_wolnosci",
              "grzywna",
              "pozbawienie_i_grzywna_zasadnicza",
              "pozbawienie_i_grzywna_art71",
              "ograniczenie_i_grzywna"
            ],
            "description": "Główny rodzaj orzeczonej kary. Rozróżnić: 'pozbawienie_i_grzywna_zasadnicza' gdy obie kary orzeczone jako zasadnicze; 'pozbawienie_i_grzywna_art71' gdy grzywna orzeczona na podst. art. 71§1 k.k. kumulatywnie przy warunkowym zawieszeniu kary pozbawienia wolności. Przy wyroku łącznym (is_aggregate_sentence = true) raportować typ kary łącznej. Null gdy verdict_type = 'warunkowe_umorzenie'.",
            "name": "sentence_type"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wymiar orzeczonej kary pozbawienia wolności w miesiącach (np. 2 lata = 24 miesiące). Przy wyroku łącznym (is_aggregate_sentence = true) podawać wymiar kary łącznej, nie kary jednostkowej za czyn narkotykowy. Pole wypełniane wyłącznie gdy sentence_type to 'pozbawienie_wolnosci', 'pozbawienie_i_grzywna_zasadnicza' lub 'pozbawienie_i_grzywna_art71'. Null jeśli nie orzeczono kary pozbawienia wolności lub verdict_type = 'warunkowe_umorzenie'.",
            "name": "imprisonment_duration_months"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wykonanie orzeczonej kary pozbawienia wolności zostało warunkowo zawieszone na podstawie art. 69–72 k.k. False jeśli kara bezwzględna lub nie orzeczono kary pozbawienia wolności.",
            "name": "sentence_suspended"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Okres próby przy zawieszeniu wykonania kary (art. 69–72 k.k.) lub warunkowym umorzeniu postępowania (art. 66–67 k.k.), wyrażony w miesiącach. Null jeśli żadna z tych instytucji nie była stosowana.",
            "name": "probation_period_months"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Wymiar orzeczonej kary ograniczenia wolności w miesiącach. Przy wyroku łącznym raportować wymiar kary łącznej. Null jeśli nie orzeczono kary ograniczenia wolności.",
            "name": "restriction_of_liberty_months"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba stawek dziennych grzywny orzeczonej przez sąd. Wartość 0 jeśli grzywna orzeczona jest jako kwota łączna bez stawek (wówczas wypełnić fine_amount_pln kwotą łączną). Null jeśli grzywny nie orzeczono.",
            "name": "fine_daily_rate_count"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota grzywny w złotych (PLN): wysokość jednej stawki dziennej jeśli grzywna orzeczona w stawkach (fine_daily_rate_count > 0), albo łączna kwota grzywny jeśli orzeczona bez stawek dziennych (fine_daily_rate_count = 0). Null jeśli grzywny nie orzeczono.",
            "name": "fine_amount_pln"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota nawiązki orzeczonej na podstawie art. 70 ust. 4 ustawy o przeciwdziałaniu narkomanii (nawiązka na cel zapobiegania narkomanii), wyrażona w złotych (PLN). Null jeśli nawiązki nie orzeczono lub nie jest możliwe ustalenie kwoty z treści dokumentu. Pole uzupełnia 'additional_penal_measures' umożliwiając ilościową analizę tego środka karnego.",
            "name": "compensatory_measure_amount_pln"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Kwota przepadku korzyści majątkowej orzeczonego na podstawie art. 45 §1 k.k. (przepadek równowartości korzyści uzyskanych z przestępstwa), wyrażona w złotych (PLN). Odrębne od nawiązki z art. 70 ust. 4 u.p.n. (compensatory_measure_amount_pln) — oba środki mogą być orzeczone łącznie. Szukać w sentencji wyroku fraz 'przepadek korzyści majątkowej', 'art. 45 §1 k.k.', 'zobowiązuje do zwrotu'. Null jeśli przepadku korzyści nie orzeczono lub nie jest możliwe ustalenie kwoty z treści dokumentu.",
            "name": "forfeiture_amount_pln"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy orzeczona kara pozbawienia wolności lub ograniczenia wolności jest równa dolnej granicy ustawowego zagrożenia przewidzianego w zastosowanym przepisie (np. 3 lata przy zbrodni z art. 53 ust. 2 u.p.n., 1 rok przy art. 62 ust. 2 u.p.n.). Kluczowe przy zbrodniach narkotykowych, gdzie kara na minimum ustawowym ma inne znaczenie analityczne niż ta sama wartość przy przestępstwie zagrożonym od 6 miesięcy. Null jeśli nie można ustalić ustawowego minimum z treści dokumentu.",
            "name": "sentence_at_statutory_minimum"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wyrok jest wyrokiem łącznym obejmującym czyny narkotykowe i inne przestępstwa (kara łączna z art. 85–91 k.k.). Pole kluczowe dla poprawnej interpretacji wymiaru kary — wyroki łączne nie są bezpośrednio porównywalne z karami jednostkowymi.",
            "name": "is_aggregate_sentence"
          },
          {
            "type_": "enum",
            "enum_name": "AggregateSentencePrinciple",
            "enum_values": [
              "absorpcja",
              "kumulacja",
              "asperacja",
              "nie_dotyczy"
            ],
            "description": "Zasada wymiaru kary łącznej zastosowana przez sąd przy wyroku łącznym (is_aggregate_sentence = true): absorpcja (kara łączna = najwyższa z kar jednostkowych), kumulacja (kara łączna = suma kar jednostkowych), asperacja (kara łączna między najwyższą a sumą kar jednostkowych). Wartość 'nie_dotyczy' gdy is_aggregate_sentence = false. Pole niezbędne do poprawnej interpretacji imprisonment_duration_months przy wyrokach łącznych.",
            "name": "aggregate_sentence_principle"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd zastosował przepisy ustawy względniejszej na podstawie art. 4 §1 k.k. (lex mitior). True gdy dokument zawiera wyraźną wzmiankę o art. 4 §1 k.k. LUB gdy z kontekstu wynika zastosowanie ustawy w brzmieniu wcześniejszym niż obowiązujące w dacie czynu (np. sąd powołuje przepisy ustawy z roku X do czynu popełnionego po nowelizacji, lub explicite wskazuje 'ustawa w brzmieniu obowiązującym w dacie czynu'). Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "favorable_law_applied_art4_kk"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w uzasadnieniu orzeczenia pojawia się jakakolwiek wzmianka o art. 62a u.p.n. (umorzenie wobec posiadacza na własny użytek w nieznacznej ilości) — obejmuje zastosowanie, rozważanie oraz odmowę zastosowania.",
            "name": "art_62a_mentioned"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy art. 62a u.p.n. został faktycznie zastosowany przez sąd lub prokuratora jako podstawa umorzenia postępowania (a nie wyłącznie wzmiankowany lub rozważany i odrzucony). True tylko przy faktycznym umorzeniu w trybie art. 62a u.p.n.",
            "name": "art_62a_actually_applied"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd powołał się na art. 54 k.k. (dyrektywy wymiaru kary wobec młodocianego — pierwszeństwo celów wychowawczych) przy uzasadnieniu wymiaru kary. Koreluje z polem defendant_is_young_adult. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "art_54_kk_applied"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd zastosował nadzwyczajne złagodzenie kary na podstawie art. 60 k.k. — obniżenie kary poniżej ustawowego minimum lub jej nadzwyczajne złagodzenie z przyczyn przewidzianych przez kodeks.",
            "name": "extraordinary_mitigation_applied"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd zastosował nadzwyczajne obostrzenie kary (np. na podstawie art. 64 k.k. w związku z recydywą lub innej podstawy ustawowej) skutkujące podwyższeniem górnej granicy ustawowego zagrożenia karą.",
            "name": "extraordinary_aggravation_applied"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy oskarżony złożył wniosek o dobrowolne poddanie się karze w trybie art. 387 k.p.k. (wniosek oskarżonego o skazanie bez przeprowadzenia postępowania dowodowego). Istotna zmienna procesowa korelująca z wymiarem kary.",
            "name": "voluntary_submission_art387"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy wniosek o skazanie bez rozprawy złożył prokurator w trybie art. 335 k.p.k. Uzupełnienie pola voluntary_submission_art387 — oba tryby konsensualne wpływają na wymiar kary, lecz różnią się inicjatorem i procedurą.",
            "name": "voluntary_submission_art335"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd orzekł środki karne lub zabezpieczające obok kary głównej (np. przepadek korzyści majątkowej lub przedmiotów służących do popełnienia przestępstwa, zakaz prowadzenia pojazdów, obowiązek poddania się leczeniu odwykowemu jako środek karny, nawiązka z art. 70 ust. 4 u.p.n.). Kwotę nawiązki rejestruje osobno pole compensatory_measure_amount_pln, kwotę przepadku korzyści rejestruje osobno pole forfeiture_amount_pln. Dozór kuratora rejestruje osobno pole probation_supervision_ordered.",
            "name": "additional_penal_measures"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd orzekł dozór kuratora sądowego na podstawie art. 73 §2 k.k. (obowiązkowy dozór przy zawieszeniu kary wobec młodocianego) lub art. 73 §1 k.k. (facultatywny dozór). Szczególnie istotne przy analizie wyroków wobec oskarżonych w kategorii wiekowej młodocianych (defendant_is_young_adult = true). False gdy dozoru nie orzeczono. Null gdy sentence_suspended = false i verdict_type != 'warunkowe_umorzenie'.",
            "name": "probation_supervision_ordered"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy przy warunkowym umorzeniu postępowania (verdict_type = 'warunkowe_umorzenie') sąd nałożył na oskarżonego obowiązki probacyjne (np. obowiązek poddania się leczeniu odwykowemu, zakaz używania środków odurzających, obowiązek naprawienia szkody). False gdy verdict_type = 'wyrok_skazujacy' lub gdy warunkowe umorzenie orzeczono bez obowiązków.",
            "name": "conditional_discontinuation_obligations"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność łagodząca wskazana przez sąd: oskarżony nie był uprzednio karany sądownie (niekaralność w chwili czynu lub orzekania). Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "mitigating_no_prior_convictions"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność łagodząca wskazana przez sąd: oskarżony przyznał się do winy w toku postępowania przygotowawczego lub sądowego. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "mitigating_confession"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność łagodząca wskazana przez sąd: oskarżony współpracował z organami ścigania (np. ujawnił innych sprawców, wskazał źródło narkotyków, złożył obszerne wyjaśnienia). Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "mitigating_cooperation_with_authorities"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność łagodząca wskazana przez sąd: środki były przeznaczone wyłącznie na własny użytek oskarżonego, powołana explicite jako przesłanka łagodząca wymiar kary. Odróżnić od possession_purpose — niniejsze pole dotyczy wyłącznie sytuacji, gdy sąd wprost wskazał własny użytek jako okoliczność łagodzącą w rozważaniach o wymiarze kary. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "mitigating_own_use_only"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność łagodząca wskazana przez sąd: oskarżony podjął lub deklarował podjęcie leczenia odwykowego lub terapii uzależnień w toku postępowania. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "mitigating_treatment_undertaken"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy sąd ustalił uzależnienie oskarżonego od środków odurzających lub substancji psychotropowych jako fakt (np. na podstawie opinii biegłego lub dokumentacji medycznej). Pole rejestruje sam fakt stwierdzenia uzależnienia, niezależnie od tego, czy było ono traktowane jako okoliczność łagodząca — zob. pole addiction_treated_as_mitigating. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "defendant_addiction_found"
          },
          {
            "type_": "enum",
            "enum_name": "AddictionMitigatingAssessment",
            "enum_values": [
              "tak",
              "nie",
              "niejednoznaczne"
            ],
            "description": "Czy sąd wprost potraktował stwierdzone uzależnienie oskarżonego jako okoliczność łagodzącą przy wymiarze kary. Wartość 'tak' gdy sąd explicite wskazuje uzależnienie jako łagodzące; 'nie' gdy sąd explicite odmawia traktowania uzależnienia jako łagodzącego; 'niejednoznaczne' gdy sformułowanie sądu jest ambiwalentne. Null gdy defendant_addiction_found = false, has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'] lub sąd w ogóle nie odnosi się do wpływu uzależnienia na wymiar kary.",
            "name": "addiction_treated_as_mitigating"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność obciążająca wskazana przez sąd: oskarżony działał w celu osiągnięcia korzyści majątkowej z obrotu narkotykami (motyw finansowy jako element kwalifikacji lub uzasadnienia surowości kary). Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "aggravating_financial_motive"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność obciążająca wskazana przez sąd: oskarżony działał w zorganizowanej grupie przestępczej lub związku mającym na celu popełnienie przestępstwa. Jeśli art. 258 k.k. stanowi odrębny zarzut, odnotować dodatkowo w parallel_offenses_present i parallel_offense_type. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "aggravating_organized_group"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność obciążająca wskazana przez sąd: przestępstwo narkotykowe popełniono w formie współsprawstwa z innymi osobami (art. 18 §1 k.k.). Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "aggravating_co_perpetration"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Okoliczność obciążająca wskazana przez sąd: oskarżony był uprzednio karany sądownie (karalność jako czynnik obciążający, niezależnie od formalnej recydywy z art. 64 k.k.). Pole może być true przy recidivism_type = 'brak' gdy oskarżony był karany, lecz nie spełnia przesłanek art. 64 k.k. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "aggravating_prior_convictions"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba poprzednich skazań za przestępstwa narkotykowe (z ustawy o przeciwdziałaniu narkomanii) wskazana lub możliwa do ustalenia z treści dokumentu. Wartość 0 gdy oskarżony nie był wcześniej karany za przestępstwa narkotykowe. Null gdy informacja niedostępna lub has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'].",
            "name": "prior_drug_convictions_count"
          },
          {
            "type_": "enum",
            "enum_name": "RecidivismType",
            "enum_values": [
              "brak",
              "podstawowa_art64_par1",
              "wielokrotna_art64_par2"
            ],
            "description": "Typ recydywy stwierdzony przez sąd na podstawie art. 64 k.k.: brak formalnej recydywy, recydywa podstawowa (art. 64 §1 k.k.) lub recydywa wielokrotna (art. 64 §2 k.k.). Wartość 'brak' oznacza brak formalnej recydywy z art. 64 k.k. — niezależnie od ewentualnej uprzedniej karalności rejestrowanej w aggravating_prior_convictions. Null gdy has_full_reasoning in ['uzasadnienie_odwolawcze', 'brak_uzasadnienia'] i brak wzmianki o recydywie w sentencji.",
            "name": "recidivism_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w tej samej sprawie oskarżonemu przypisano równoległe czyny zabronione spoza ustawy o przeciwdziałaniu narkomanii (z Kodeksu karnego lub innych ustaw szczególnych).",
            "name": "parallel_offenses_present"
          },
          {
            "type_": "integer",
            "enum_name": null,
            "enum_values": [],
            "description": "Liczba równoległych czynów zabronionych spoza ustawy o przeciwdziałaniu narkomanii przypisanych oskarżonemu w tym samym postępowaniu. Wartość 0 jeśli parallel_offenses_present = false.",
            "name": "parallel_offense_count"
          },
          {
            "type_": "enum",
            "enum_name": "ParallelOffenseType",
            "enum_values": [
              "art_178a_kk_jazda_pod_wplywem",
              "art_157_kk_uszczerbek_na_zdrowiu",
              "art_258_kk_zorganizowana_grupa",
              "art_263_kk_nielegalne_posiadanie_broni",
              "inne",
              "brak"
            ],
            "description": "Główny (najpoważniejszy) typ równoległego czynu zabronionego przypisanego oskarżonemu w tym samym postępowaniu. Przy wielu równoległych czynach wskazać najpoważniejszy — ich łączną liczbę rejestruje parallel_offense_count, a pełną listę artykułów rejestruje parallel_offense_articles. Wartość 'brak' gdy parallel_offenses_present = false.",
            "name": "parallel_offense_type"
          },
          {
            "type_": "string",
            "enum_name": null,
            "enum_values": [],
            "description": "Lista wszystkich artykułów równoległych czynów zabronionych przypisanych oskarżonemu w tym samym postępowaniu, podana jako tekst rozdzielony przecinkami (np. 'art. 178a §1 k.k., art. 157 §1 k.k.'). Uzupełnienie pól parallel_offense_count i parallel_offense_type umożliwiające pełną analizę współwystępowania czynów. Null jeśli parallel_offenses_present = false.",
            "name": "parallel_offense_articles"
          }
        ]
        ```

=== "Gemma 4 E4B IT"

    **25 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `typ_orzeczenia` | enum | Type of ruling under analysis — must be a conviction or an order of conditional discontinuation. |
        | `podstawa_czynu_prawnie` | string | Main legal basis classifying the offense (e.g. Art. 62 of the Drug Act, Art. 157 Penal Code). |
        | `typ_czynu_wg_artykulu` | enum | More detailed classification of the offense under the Drug Act (e.g. possession, dealing, production). |
        | `rodzaj_substancji` | string | Specific type of narcotic or psychotropic substance. |
        | `cel_posiadania` | enum | Declared or established purpose of possessing the substance. |
        | `sąd_wydayacy` | string | Name or code of the court that issued the ruling. |
        | `case_id` | string | Unique identifier of the court case (case number). |
        | `faza_postepowania_orzeczenie` | string | Procedural phase in which the ruling was issued. |
        | `data_urodzenia_oskarzonego` | string | Defendant's date of birth. |
        | `kategoria_wieku_prawne` | enum | Defendant's age category under procedural definitions (baseline). |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `typ_orzeczenia` | enum | Typ orzeczenia, które jest przedmiotem analizy. Musi być skazujące lub postanowienie o warunkowym umorzeniu. Wydobywane z nagłówka lub części rozpoznawczej. |
        | `podstawa_czynu_prawnie` | string | Główna podstawa prawna kwalifikująca czyn (np. Art. 62 Ustawy, Art. 157 KK). Wymaga ekstrakcji pełnego brzmienia lub odniesienia. |
        | `typ_czynu_wg_artykulu` | enum | Bardziej szczegółowa kwalifikacja czynu zgodnie z Ustawą o przeciwdziałaniu narkomanii (np. posiadanie, obrót, wytwarzanie). |
        | `rodzaj_substancji` | string | Konkretny rodzaj środka odurzającego lub substancji psychotropowej. Wymaga kontekstualizacji z opisem czynu. |
        | `cel_posiadania` | enum | Zadeklarowany lub ustalone w sprawie cel posiadania substancji. Często podane w uzasadnieniu. |
        | `sąd_wydayacy` | string | Nazwa lub kod sądu, który wydał orzeczenie. Pomaga w analizie rozkładu orzeczeń. |
        | `case_id` | string | Unikalny identyfikator sprawy sądowej (sygnatura). |
        | `faza_postepowania_orzeczenie` | string | Faza postępowania, w której wydano orzeczenie. Pomaga w kontekstualizacji rozstrzygnięcia. |
        | `data_urodzenia_oskarzonego` | string | Data urodzenia oskarżonego. Jest to kluczowa informacja dla kategoryzacji wiekowej. |
        | `kategoria_wieku_prawne` | enum | Kategoria wieku oskarżonego zgodnie z definicjami procesowymi (bazowa). |
    ??? note "Show full schema (25 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "enum",
            "enum_name": "Typ_Orzeczenia",
            "enum_values": [
              "Wyrok_Skazujący",
              "Postanowienie_o_Warunkowym_Umorzeniu"
            ],
            "description": "Typ orzeczenia, które jest przedmiotem analizy. Musi być skazujące lub postanowienie o warunkowym umorzeniu. Wydobywane z nagłówka lub części rozpoznawczej.",
            "name": "typ_orzeczenia"
          },
          {
            "type_": "string",
            "enum_name": "Podstawa_Czynu_Prawnie",
            "enum_values": [
              "Art. Ustawy o Przeciwdziałaniu Narkomanii",
              "Art. Kodeksu Karnego",
              "Inna Podstawa Prawna"
            ],
            "description": "Główna podstawa prawna kwalifikująca czyn (np. Art. 62 Ustawy, Art. 157 KK). Wymaga ekstrakcji pełnego brzmienia lub odniesienia.",
            "name": "podstawa_czynu_prawnie"
          },
          {
            "type_": "enum",
            "enum_name": "Typ_Czynu_Wg_Artykulu",
            "enum_values": [
              "Posiadanie",
              "Obrót",
              "Wytwarzanie",
              "Przewóz",
              "Inne_Narkotykowe"
            ],
            "description": "Bardziej szczegółowa kwalifikacja czynu zgodnie z Ustawą o przeciwdziałaniu narkomanii (np. posiadanie, obrót, wytwarzanie).",
            "name": "typ_czynu_wg_artykulu"
          },
          {
            "type_": "string",
            "enum_name": "Rodzaj_Substancji_Konkretny",
            "enum_values": [
              "Marihuana",
              "Kokaina",
              "Amfetamina",
              "Krystaliczny_Metamfetamin",
              "Inna_Konkretna"
            ],
            "description": "Konkretny rodzaj środka odurzającego lub substancji psychotropowej. Wymaga kontekstualizacji z opisem czynu.",
            "name": "rodzaj_substancji"
          },
          {
            "type_": "enum",
            "enum_name": "Cel_Posiadania",
            "enum_values": [
              "Na_Wlasny_Uzytek",
              "Cel_Obrotowy",
              "Nieokreślony"
            ],
            "description": "Zadeklarowany lub ustalone w sprawie cel posiadania substancji. Często podane w uzasadnieniu.",
            "name": "cel_posiadania"
          },
          {
            "type_": "string",
            "enum_name": "Sąd_Wydayacy",
            "enum_values": [
              "Wydział_Karny_I",
              "Sąd_Rejonowy_X",
              "Apelacyjny_Y"
            ],
            "description": "Nazwa lub kod sądu, który wydał orzeczenie. Pomaga w analizie rozkładu orzeczeń.",
            "name": "sąd_wydayacy"
          },
          {
            "type_": "string",
            "enum_name": "Case_ID",
            "enum_values": [
              "String_ID"
            ],
            "description": "Unikalny identyfikator sprawy sądowej (sygnatura).",
            "name": "case_id"
          },
          {
            "type_": "string",
            "enum_name": "Faza_Postepowania_Orzeczenie",
            "enum_values": [
              "Pierwsza Instancja",
              "Apelacja",
              "Kasacja"
            ],
            "description": "Faza postępowania, w której wydano orzeczenie. Pomaga w kontekstualizacji rozstrzygnięcia.",
            "name": "faza_postepowania_orzeczenie"
          },
          {
            "type_": "string",
            "enum_name": "Data_Urodzenia_Oskarzonego",
            "enum_values": [
              "YYYY-MM-DD"
            ],
            "description": "Data urodzenia oskarżonego. Jest to kluczowa informacja dla kategoryzacji wiekowej.",
            "name": "data_urodzenia_oskarzonego"
          },
          {
            "type_": "enum",
            "enum_name": "Kategoria_Wieku_Prawna_Bazowa",
            "enum_values": [
              "Nieletni",
              "Młodociany_Art_115",
              "Dorosły"
            ],
            "description": "Kategoria wieku oskarżonego zgodnie z definicjami procesowymi (bazowa).",
            "name": "kategoria_wieku_prawne"
          },
          {
            "type_": "enum",
            "enum_name": "Przedzial_Wiekowy_Analiza",
            "enum_values": [
              "0-17",
              "18-21",
              "22-39",
              "40-59",
              "60+"
            ],
            "description": "Przedział wiekowy (w latach) oskarżonego, obliczony na podstawie 'data_urodzenia_oskarzonego'. Używać tylko jeśli data urodzenia jest dostępna.",
            "name": "przedzial_wiekowy_analiza"
          },
          {
            "type_": "integer",
            "enum_name": "Liczba_Czynów_Agregowanych",
            "enum_values": [
              "1"
            ],
            "description": "Liczba czynów przestępczych, które zostały zsumowane do wydania tego orzeczenia (ważne w przypadku wyroków łącznych). Domyślnie 1.",
            "name": "liczba_czynów_agregowanych"
          },
          {
            "type_": "float",
            "enum_name": "Miar_Kary_W_Dniach",
            "enum_values": [
              "0.0"
            ],
            "description": "Ostateczny wymiar kary pozbawienia wolności wyrażony w dniach. W przypadku kar łącznych, jest to wynik sumowania lub orzeczenia o karze łącznej.",
            "name": "miar_kary_w_dnach"
          },
          {
            "type_": "enum",
            "enum_name": "Warunkowe_Umorzenie_Zastosowano",
            "enum_values": [
              "Tak",
              "Nie"
            ],
            "description": "Wskazuje, czy sąd zastosował postanowienie o warunkowym umorzeniu postępowania.",
            "name": "warunkowe_umorzenie_zastosowano"
          },
          {
            "type_": "float",
            "enum_name": "Okres_Proby_Lat",
            "enum_values": [
              "0.0"
            ],
            "description": "Określony okres próby (w latach) w przypadku zawieszenia kary lub warunkowego umorzenia.",
            "name": "okres_proby_lat"
          },
          {
            "type_": "float",
            "enum_name": "Kwota_Nawiazki_PLN",
            "enum_values": [
              "0.0"
            ],
            "description": "Określona kwota nawiązki (w PLN). Używać 0.0, jeśli nie została orzeczona.",
            "name": "kwota_nawiazki"
          },
          {
            "type_": "float",
            "enum_name": "Koszty_Sadowe_PLN",
            "enum_values": [
              "0.0"
            ],
            "description": "Określone koszty sądowe. Używać 0.0, jeśli nie dotyczy.",
            "name": "koszty_sadowe"
          },
          {
            "type_": "boolean",
            "enum_name": "Obecnosc_Rownolegle_Czyny",
            "enum_values": [
              "true",
              "false"
            ],
            "description": "Wskazuje, czy w sprawie rozpatrywano równoległe czyny przestępcze (nawet jeśli zostały one skonsolidowane w jednym orzeczeniu).",
            "name": "obecnosc_rownoległych_czynów"
          },
          {
            "type_": "boolean",
            "enum_name": "Jest_Recydywa",
            "enum_values": [
              "true",
              "false"
            ],
            "description": "Wskazuje, czy orzeczenie opiera się na stwierdzonej recydywie (ważny czynnik obciążający).",
            "name": "jest_recydywa"
          },
          {
            "type_": "enum",
            "enum_name": "Status_Uzaleznienia",
            "enum_values": [
              "Potwierdzone_W_Sprawie",
              "Niepotwierdzone",
              "Nie_Wskazane"
            ],
            "description": "Status uzależnienia oskarżonego uznany przez sąd lub wskazany w uzasadnieniu (ważny czynnik łagodzący/obciążający).",
            "name": "status_uzalezdenia"
          },
          {
            "type_": "boolean",
            "enum_name": "Korzyść_Majatkowa_Osiągnięta",
            "enum_values": [
              "true",
              "false"
            ],
            "description": "Czy czyn był popełniony w celu osiągnięcia korzyści majątkowej (czynnik obciążający).",
            "name": "korzyść_majatkowa_osiągnięta"
          },
          {
            "type_": "boolean",
            "enum_name": "Wspolsprawstwo_Wielopodmiotowe",
            "enum_values": [
              "true",
              "false"
            ],
            "description": "Czy oskarżony był współsprawcą lub uczestnikiem czynu z innymi osobami (czynnik obciążający).",
            "name": "wspolsprawstwo_wielopodmiotowe"
          },
          {
            "type_": "enum",
            "enum_name": "Stopien_Szkodliwosci_Czynu",
            "enum_values": [
              "Niski",
              "Średni",
              "Wysoki"
            ],
            "description": "Ocena sądu dotycząca społecznej szkodliwości czynu.",
            "name": "stopien_szkodliwosci_czynu"
          },
          {
            "type_": "float",
            "enum_name": "Wartosc_Iloscy_Substancji",
            "enum_values": [
              "0.0"
            ],
            "description": "Ilość substancji w jednostkach określonych w polu 'jednostka_iloscy'.",
            "name": "wartosc_iloscy"
          },
          {
            "type_": "string",
            "enum_name": "Jednostka_Substancji",
            "enum_values": [
              "mg",
              "g",
              "kg",
              "inne"
            ],
            "description": "Jednostka miary ilości substancji (np. g, mg).",
            "name": "jednostka_iloscy"
          }
        ]
        ```

=== "GPT-5.4 nano"

    **24 fields total.** Below are the first 10 fields, in schema order; the full schema is available raw beneath it.

    === "🇬🇧 English"

        | Field | Type | Description |
        |---|---|---|
        | `appeal_procedure_relevant_to_this_sentence` | boolean | Whether this part of the document indicates the case is on appeal, or that the sentence was changed as part of this decision. |
        | `appeal_sentence_changed` | boolean | Whether the ruling changed a previously imposed sentence as a result of an appeal. |
        | `appeal_change_type` | enum | Direction of the sentence change resulting from the appeal. |
        | `defendant_1_age_years_available` | boolean | Whether a numeric age can be computed for defendant slot 1. |
        | `defendant_1_age_bucket_5_from_text_present` | enum | Whether a 5-way age bucket can be assigned for slot 1 from qualitative descriptions alone. |
        | `defendant_1_age_bucket_5_from_text` | enum | The 5-way age bucket for slot 1 derived from descriptive text. |
        | `defendant_1_narcotics_role_in_this_outcome` | enum | Role of narcotics in this specific ruling for defendant slot 1. |
        | `defendant_1_drug_amount_info_present` | enum | Whether the text provides drug-amount information for slot 1. |
        | `defendant_1_drug_substance_type_info_present` | enum | Whether the text provides substance-type information for slot 1. |
        | `defendant_1_drug_action_purpose_info_present` | enum | Whether the text provides information on the purpose of the act (own use vs. dealing) for slot 1. |

    === "🇵🇱 Polski"

        | Field | Type | Description |
        |---|---|---|
        | `appeal_procedure_relevant_to_this_sentence` | boolean | Czy w samej treści/tym fragmencie dokumentu (sentencja lub jednoznaczny opis rozstrzygnięcia w uzasadnieniu) pojawia się informacja, że sprawa ma charakter odwoławczy / rozpoznano apelację lub zmieniono karę w ramach tej właśnie decyzji? Ustawiaj true tylko, gdy apelacja/zmiana w zakresie kary jest wprost istotna dla tego dokumentu; false gdy wzmianka o postępowaniu odwoławczym występuje tylko jako tło w innych sprawach. |
        | `appeal_sentence_changed` | boolean | Czy rozstrzygnięcie zmieniło uprzednio orzeczoną karę/jej dolegliwość wskutek środka odwoławczego. Koduj tylko jeśli `appeal_procedure_relevant_to_this_sentence=true` oraz decyzja jest odwoławcza (np. `decision_procedure_stage=odwoławcze`); w przeciwnym razie ustaw false. |
        | `appeal_change_type` | enum | Kierunek zmiany kary na skutek apelacji/odwołania. Koduj tylko jeśli `appeal_procedure_relevant_to_this_sentence=true` i `decision_procedure_stage=odwoławcze`; w przeciwnym razie ustaw `nieustalone`. |
        | `defendant_1_age_years_available` | boolean | Czy dla slota 1 da się wyliczyć wiek liczbowo (np. na podstawie pełnej daty urodzenia + daty czynu/ustalenia, albo na podstawie wskazanego wprost wieku). Jeśli dokument podaje tylko „urodz. (...)” bez daty dziennej/pełnej — ustaw false. |
        | `defendant_1_age_bucket_5_from_text_present` | enum | Czy dla slota 1 da się przypisać bucket 5 wyłącznie z opisów jakościowych (np. „w wieku nastoletnim”, „nieletni”, „w wieku około 20 lat”), mimo braku możliwości wyliczenia wieku liczbowo? |
        | `defendant_1_age_bucket_5_from_text` | enum | Bucket 5 dla slota 1 wyznaczony z treści opisowej, gdy `defendant_1_age_bucket_5_from_text_present=tak`. Jeśli nie da się w sposób odtwarzalny przypisać, ustaw `brak_danych`. Buckety interpretuj zgodnie z `age_bucket_scheme_definition`. |
        | `defendant_1_narcotics_role_in_this_outcome` | enum | Rola narkotyków w tym rozstrzygnięciu dla slota 1: `dominujący_w_tym_orzeczeniu`, gdy w tej decyzji sąd faktycznie rozstrzyga w oparciu o ustalenia dotyczące narkotyków (kwalifikacja i/lub opis faktów o substancjach/ilości/celu w kontekście kary); `tylko_w_tle_wyrokow_jednostkowych`, gdy dokument ma charakter wyroku łącznego i szczegóły narkotykowe są jedynie „w tle” kar jednostkowych bez ponownego ustalania; `nie_dotyczy_w_tym_orzeczeniu`, gdy w tej decyzji nie ma odniesień do narkotyków; `nieustalone`, gdy nie da się tego rozstrzygnąć. |
        | `defendant_1_drug_amount_info_present` | enum | Czy w tekście dla slota 1 jest informacja o ilości (waga/objętość/liczba jednostek) dotycząca narkotyków w kontekście tej decyzji? `ilość_wprost` gdy jest podana ilość; `ilość_pośrednio` gdy ilość wynika z przeliczeń/danych zastępczych w opisie; `brak_ilości_opisu` gdy nie ma ilości; `nieustalone` gdy nie da się ocenić. |
        | `defendant_1_drug_substance_type_info_present` | enum | Czy w tekście dla slota 1 jest informacja o rodzaju substancji? `substancja_wprost` gdy nazwa grupy/konkretnej substancji jest wskazana wprost; `substancja_pośrednio` gdy wynika z kwalifikacji lub opisu bez pełnej nazwy; `brak_substancji_opisu` gdy nie ma informacji; `nieustalone` gdy nie da się ocenić. |
        | `defendant_1_drug_action_purpose_info_present` | enum | Czy w tekście dla slota 1 jest informacja o celu działania (np. własny użytek vs obrót/korzyść) w kontekście tej decyzji? `cel_wprost` gdy jest wskazany wprost; `cel_pośrednio` gdy cel wynika z okoliczności opisanych przez sąd; `brak_opisu_celu` gdy nie ma opisu celu; `nieustalone` gdy nie da się ocenić. |
    ??? note "Show full schema (24 fields, raw JSON, original language)"

        ```json
        [
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy w samej treści/tym fragmencie dokumentu (sentencja lub jednoznaczny opis rozstrzygnięcia w uzasadnieniu) pojawia się informacja, że sprawa ma charakter odwoławczy / rozpoznano apelację lub zmieniono karę w ramach tej właśnie decyzji? Ustawiaj true tylko, gdy apelacja/zmiana w zakresie kary jest wprost istotna dla tego dokumentu; false gdy wzmianka o postępowaniu odwoławczym występuje tylko jako tło w innych sprawach.",
            "name": "appeal_procedure_relevant_to_this_sentence"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy rozstrzygnięcie zmieniło uprzednio orzeczoną karę/jej dolegliwość wskutek środka odwoławczego. Koduj tylko jeśli `appeal_procedure_relevant_to_this_sentence=true` oraz decyzja jest odwoławcza (np. `decision_procedure_stage=odwoławcze`); w przeciwnym razie ustaw false.",
            "name": "appeal_sentence_changed"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "zaostrzenie",
              "zlagodzenie",
              "zmiana_rodzaju_kary",
              "nieustalone"
            ],
            "description": "Kierunek zmiany kary na skutek apelacji/odwołania. Koduj tylko jeśli `appeal_procedure_relevant_to_this_sentence=true` i `decision_procedure_stage=odwoławcze`; w przeciwnym razie ustaw `nieustalone`.",
            "name": "appeal_change_type"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dla slota 1 da się wyliczyć wiek liczbowo (np. na podstawie pełnej daty urodzenia + daty czynu/ustalenia, albo na podstawie wskazanego wprost wieku). Jeśli dokument podaje tylko „urodz. (...)” bez daty dziennej/pełnej — ustaw false.",
            "name": "defendant_1_age_years_available"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Czy dla slota 1 da się przypisać bucket 5 wyłącznie z opisów jakościowych (np. „w wieku nastoletnim”, „nieletni”, „w wieku około 20 lat”), mimo braku możliwości wyliczenia wieku liczbowo?",
            "name": "defendant_1_age_bucket_5_from_text_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "bucket_1",
              "bucket_2",
              "bucket_3",
              "bucket_4",
              "bucket_5",
              "brak_danych"
            ],
            "description": "Bucket 5 dla slota 1 wyznaczony z treści opisowej, gdy `defendant_1_age_bucket_5_from_text_present=tak`. Jeśli nie da się w sposób odtwarzalny przypisać, ustaw `brak_danych`. Buckety interpretuj zgodnie z `age_bucket_scheme_definition`.",
            "name": "defendant_1_age_bucket_5_from_text"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "dominujący_w_tym_orzeczeniu",
              "tylko_w_tle_wyrokow_jednostkowych",
              "nie_dotyczy_w_tym_orzeczeniu",
              "nieustalone"
            ],
            "description": "Rola narkotyków w tym rozstrzygnięciu dla slota 1: `dominujący_w_tym_orzeczeniu`, gdy w tej decyzji sąd faktycznie rozstrzyga w oparciu o ustalenia dotyczące narkotyków (kwalifikacja i/lub opis faktów o substancjach/ilości/celu w kontekście kary); `tylko_w_tle_wyrokow_jednostkowych`, gdy dokument ma charakter wyroku łącznego i szczegóły narkotykowe są jedynie „w tle” kar jednostkowych bez ponownego ustalania; `nie_dotyczy_w_tym_orzeczeniu`, gdy w tej decyzji nie ma odniesień do narkotyków; `nieustalone`, gdy nie da się tego rozstrzygnąć.",
            "name": "defendant_1_narcotics_role_in_this_outcome"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "ilość_wprost",
              "ilość_pośrednio",
              "brak_ilości_opisu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 1 jest informacja o ilości (waga/objętość/liczba jednostek) dotycząca narkotyków w kontekście tej decyzji? `ilość_wprost` gdy jest podana ilość; `ilość_pośrednio` gdy ilość wynika z przeliczeń/danych zastępczych w opisie; `brak_ilości_opisu` gdy nie ma ilości; `nieustalone` gdy nie da się ocenić.",
            "name": "defendant_1_drug_amount_info_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "substancja_wprost",
              "substancja_pośrednio",
              "brak_substancji_opisu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 1 jest informacja o rodzaju substancji? `substancja_wprost` gdy nazwa grupy/konkretnej substancji jest wskazana wprost; `substancja_pośrednio` gdy wynika z kwalifikacji lub opisu bez pełnej nazwy; `brak_substancji_opisu` gdy nie ma informacji; `nieustalone` gdy nie da się ocenić.",
            "name": "defendant_1_drug_substance_type_info_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "cel_wprost",
              "cel_pośrednio",
              "brak_opisu_celu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 1 jest informacja o celu działania (np. własny użytek vs obrót/korzyść) w kontekście tej decyzji? `cel_wprost` gdy jest wskazany wprost; `cel_pośrednio` gdy cel wynika z okoliczności opisanych przez sąd; `brak_opisu_celu` gdy nie ma opisu celu; `nieustalone` gdy nie da się ocenić.",
            "name": "defendant_1_drug_action_purpose_info_present"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dla slota 2 da się wyliczyć wiek liczbowo (pełna data urodzenia i odniesienie czasowe lub wskazany wprost wiek).",
            "name": "defendant_2_age_years_available"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Czy dla slota 2 da się przypisać bucket 5 wyłącznie z opisów jakościowych, mimo braku możliwości wyliczenia wieku liczbowo?",
            "name": "defendant_2_age_bucket_5_from_text_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "bucket_1",
              "bucket_2",
              "bucket_3",
              "bucket_4",
              "bucket_5",
              "brak_danych"
            ],
            "description": "Bucket 5 dla slota 2 wyznaczony z treści opisowej, gdy `defendant_2_age_bucket_5_from_text_present=tak`. Buckety interpretuj zgodnie z `age_bucket_scheme_definition`.",
            "name": "defendant_2_age_bucket_5_from_text"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "dominujący_w_tym_orzeczeniu",
              "tylko_w_tle_wyrokow_jednostkowych",
              "nie_dotyczy_w_tym_orzeczeniu",
              "nieustalone"
            ],
            "description": "Rola narkotyków w tym rozstrzygnięciu dla slota 2 (analogicznie jak dla slota 1).",
            "name": "defendant_2_narcotics_role_in_this_outcome"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "ilość_wprost",
              "ilość_pośrednio",
              "brak_ilości_opisu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 2 jest informacja o ilości narkotyków w kontekście tej decyzji (analogicznie jak dla slota 1).",
            "name": "defendant_2_drug_amount_info_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "substancja_wprost",
              "substancja_pośrednio",
              "brak_substancji_opisu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 2 jest informacja o rodzaju substancji (analogicznie jak dla slota 1).",
            "name": "defendant_2_drug_substance_type_info_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "cel_wprost",
              "cel_pośrednio",
              "brak_opisu_celu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 2 jest informacja o celu działania (analogicznie jak dla slota 1).",
            "name": "defendant_2_drug_action_purpose_info_present"
          },
          {
            "type_": "boolean",
            "enum_name": null,
            "enum_values": [],
            "description": "Czy dla slota 3 da się wyliczyć wiek liczbowo (pełna data urodzenia i odniesienie czasowe lub wskazany wprost wiek).",
            "name": "defendant_3_age_years_available"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "tak",
              "nie",
              "nieustalone"
            ],
            "description": "Czy dla slota 3 da się przypisać bucket 5 wyłącznie z opisów jakościowych, mimo braku możliwości wyliczenia wieku liczbowo?",
            "name": "defendant_3_age_bucket_5_from_text_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "bucket_1",
              "bucket_2",
              "bucket_3",
              "bucket_4",
              "bucket_5",
              "brak_danych"
            ],
            "description": "Bucket 5 dla slota 3 wyznaczony z treści opisowej, gdy `defendant_3_age_bucket_5_from_text_present=tak`. Buckety interpretuj zgodnie z `age_bucket_scheme_definition`.",
            "name": "defendant_3_age_bucket_5_from_text"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "dominujący_w_tym_orzeczeniu",
              "tylko_w_tle_wyrokow_jednostkowych",
              "nie_dotyczy_w_tym_orzeczeniu",
              "nieustalone"
            ],
            "description": "Rola narkotyków w tym rozstrzygnięciu dla slota 3 (analogicznie jak dla slota 1).",
            "name": "defendant_3_narcotics_role_in_this_outcome"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "ilość_wprost",
              "ilość_pośrednio",
              "brak_ilości_opisu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 3 jest informacja o ilości narkotyków w kontekście tej decyzji (analogicznie jak dla slota 1).",
            "name": "defendant_3_drug_amount_info_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "substancja_wprost",
              "substancja_pośrednio",
              "brak_substancji_opisu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 3 jest informacja o rodzaju substancji (analogicznie jak dla slota 1).",
            "name": "defendant_3_drug_substance_type_info_present"
          },
          {
            "type_": "enum",
            "enum_name": null,
            "enum_values": [
              "cel_wprost",
              "cel_pośrednio",
              "brak_opisu_celu",
              "nieustalone"
            ],
            "description": "Czy w tekście dla slota 3 jest informacja o celu działania (analogicznie jak dla slota 1).",
            "name": "defendant_3_drug_action_purpose_info_present"
          }
        ]
        ```

