"""
Curated Type 2 Diabetes Mellitus (T2DM) Medical Knowledge Base.
Sources:
- American Diabetes Association (ADA) Standards of Care in Diabetes (2024)
- World Health Organization (WHO) Guidelines for Type 2 Diabetes (2023)
- Indian Council of Medical Research (ICMR) Guidelines for Management of Type 2 Diabetes (2023)
- DailyMed / US FDA Approved Drug Information
"""

from typing import List, Dict, Any
_SRC = "DailyMed / US FDA Approved Drug Information"
_SRC1 = "American Diabetes Association (ADA) Standards of Care"

T2DM_KNOWLEDGE_DOCUMENTS: List[Dict[str, Any]] = [
    {
        "id": "t2dm_fund_01",
        "topic": "Type 2 Diabetes Fundamentals",
        "title": "Pathophysiology and Diagnostic Criteria of Type 2 Diabetes Mellitus",
        "source": "American Diabetes Association (ADA) Standards of Care",
        "version": "2024",
        "section": "Classification and Diagnosis of Diabetes",
        "citation": "ADA Standards of Care in Diabetes—2024, Diabetes Care 2024;47(Suppl. 1):S20–S42",
        "content": (
            "Type 2 Diabetes Mellitus (T2DM) is characterized by progressive loss of adequate beta-cell insulin secretion "
            "frequently on the background of insulin resistance in liver, skeletal muscle, and adipose tissue. "
            "Diagnostic criteria for diabetes require one of the following confirmed by repeat testing in the absence of unequivocal hyperglycemia: "
            "1. Fasting plasma glucose (FPG) >= 126 mg/dL (7.0 mmol/L) after an 8-hour fast. "
            "2. 2-hour plasma glucose >= 200 mg/dL (11.1 mmol/L) during a 75g oral glucose tolerance test (OGTT). "
            "3. HbA1c >= 6.5% (48 mmol/mol) using an NGSP-certified assay. "
            "4. Classic symptoms of hyperglycemia or hyperglycemic crisis with a random plasma glucose >= 200 mg/dL (11.1 mmol/L). "
            "Prediabetes is defined as FPG 100-125 mg/dL (impaired fasting glucose) or 2-hour PG 140-199 mg/dL (impaired glucose tolerance) or HbA1c 5.7-6.4%."
        )
    },
    {
        "id": "t2dm_hba1c_02",
        "topic": "HbA1c Interpretation",
        "title": "Glycemic Targets and Individualization of HbA1c in T2DM",
        "source": "ADA Standards of Care",
        "version": "2024",
        "section": "Glycemic Targets",
        "citation": "ADA Standards of Care in Diabetes—2024, Diabetes Care 2024;47(Suppl. 1):S111–S125",
        "content": (
            "An HbA1c goal of < 7.0% (53 mmol/mol) is appropriate for many non-pregnant adult patients with Type 2 Diabetes "
            "to prevent or slow microvascular complications (retinopathy, nephropathy, and neuropathy). "
            "Stringent targets (< 6.5%) may be considered for younger patients with short diabetes duration, long life expectancy, "
            "and no significant cardiovascular disease if achievable without significant hypoglycemia or adverse treatment effects. "
            "Less stringent targets (< 8.0% or 8.5%) are indicated for patients with a history of severe hypoglycemia, limited life expectancy, "
            "advanced microvascular or macrovascular complications, extensive comorbid conditions, or long-standing diabetes difficult to control. "
            "HbA1c reflects average glycemia over approximately 90-120 days, weighted towards the preceding 30 days. "
            "Conditions that alter red blood cell turnover (hemoglobinopathies, severe anemia, hemodialysis) require plasma glucose or fructosamine evaluation."
        )
    },
    {
        "id": "t2dm_fbg_ppbg_03",
        "topic": "Blood Glucose Measurements",
        "title": "Fasting and Postprandial Blood Glucose Monitoring & Targets",
        "source": "World Health Organization (WHO) & ADA Standards",
        "version": "2023-2024",
        "section": "Glycemic Monitoring & Clinical Targets",
        "citation": "WHO Package of Essential NCD Interventions 2023; ADA Standards of Care 2024, Section 6",
        "content": (
            "Target preprandial (fasting) capillary blood glucose for non-pregnant adults with T2DM is 80–130 mg/dL (4.4–7.2 mmol/L). "
            "Peak postprandial capillary blood glucose (measured 1–2 hours after the start of a meal) target is < 180 mg/dL (< 10.0 mmol/L). "
            "Fasting hyperglycemia predominantly reflects excessive hepatic glucose output and basal insulin deficiency, whereas postprandial "
            "hyperglycemia reflects impaired first-phase insulin secretion and peripheral insulin resistance following carbohydrate ingestion. "
            "Marked discordance between HbA1c and fasting glucose often indicates postprandial glycemic excursions. "
            "Self-monitoring of blood glucose (SMBG) frequency should be tailored to medication regimen: higher frequency with insulin/secretagogues, "
            "and structured periodic testing for non-insulin regimens."
        )
    },
    {
        "id": "t2dm_lab_mon_04",
        "topic": "Diabetes-related Laboratory Monitoring",
        "title": "Routine Laboratory Testing Schedule for Type 2 Diabetes",
        "source": "Indian Council of Medical Research (ICMR) & ADA Standards",
        "version": "2023-2024",
        "section": "Comprehensive Medical Evaluation and Assessment of Comorbidities",
        "citation": "ICMR Guidelines for Management of Type 2 Diabetes 2023, Ch. 3; ADA Standards 2024, Section 4",
        "content": (
            "Routine laboratory monitoring for T2DM patients includes: "
            "1. HbA1c testing at least twice yearly in patients meeting glycemic goals and stable regimens; quarterly in patients whose therapy has changed or who are not meeting goals. "
            "2. Serum creatinine and calculated estimated Glomerular Filtration Rate (eGFR) at least annually (every 3–6 months if eGFR < 60 mL/min/1.73m2). "
            "3. Spot urinary albumin-to-creatinine ratio (UACR) annually to detect early diabetic kidney disease. "
            "4. Fasting lipid panel (Total cholesterol, LDL-C, HDL-C, Triglycerides) annually, or every 4-12 weeks following initiation or adjustment of lipid-lowering therapy. "
            "5. Liver function enzymes (AST, ALT) annually, especially given high prevalence of Metabolic Dysfunction-Associated Steatohepatitis (MASH). "
            "6. Serum potassium and electrolytes when prescribed ACE inhibitors, ARBs, SGLT2 inhibitors, or diuretics."
        )
    },
    {
        "id": "t2dm_med_metformin_05",
        "topic": "Medication Information",
        "title": "Metformin Pharmacology, Efficacy, and Dosing Guidelines",
        "source": "DailyMed & ADA Standards of Care",
        "version": "2024",
        "section": "Pharmacologic Approaches to Glycemic Treatment",
        "citation": "DailyMed Metformin Hydrochloride Prescribing Information; ADA Standards of Care 2024, Section 9",
        "content": (
            "Metformin (biguanide class) decreases hepatic glucose production, decreases intestinal absorption of glucose, "
            "and improves insulin sensitivity by increasing peripheral glucose uptake and utilization. "
            "Typical starting dose is 500 mg once or twice daily with meals, titrated weekly to a target dose of 1000 mg twice daily (or 2000 mg extended release once daily). "
            "Expected HbA1c reduction is approximately 1.0% to 1.5%. Metformin is weight-neutral or promotes modest weight loss and does not cause hypoglycemia as monotherapy. "
            "Common adverse reactions include gastrointestinal symptoms (diarrhea, nausea, abdominal discomfort), which can be mitigated by taking doses with meals and gradual titration. "
            "Long-term use is associated with biochemical vitamin B12 deficiency; periodic monitoring of B12 levels is recommended, especially in patients with anemia or peripheral neuropathy."
        )
    },
    {
        "id": "t2dm_med_sglt2_06",
        "topic": "Medication Information",
        "title": "SGLT2 Inhibitors (Empagliflozin, Dapagliflozin, Canagliflozin) in T2DM",
        "source": "ADA Standards of Care & DailyMed",
        "version": "2024",
        "section": "Cardiovascular and Renal Disease Risk Reduction",
        "citation": "ADA Standards of Care in Diabetes—2024, Section 10; DailyMed Empagliflozin Package Insert",
        "content": (
            "Sodium-glucose cotransporter 2 (SGLT2) inhibitors reduce renal glucose reabsorption in the proximal renal tubules, "
            "promoting urinary glucose excretion (glucosuria) independent of insulin secretion. "
            "Common agents: Empagliflozin (10-25 mg daily), Dapagliflozin (5-10 mg daily), Canagliflozin (100-300 mg daily). "
            "Key clinical benefits: significant reduction in heart failure hospitalizations, progression of chronic kidney disease (CKD), "
            "and major adverse cardiovascular events (MACE) in patients with established ASCVD or high risk. "
            "Glycemic efficacy decreases with declining renal function (minimal glucose lowering when eGFR < 45 mL/min/1.73m2), "
            "yet renoprotective and cardioreprotective benefits persist down to eGFR 20 mL/min/1.73m2. "
            "Adverse risks: mycotic genital infections, urinary tract infections, volume depletion, and rare euglycemic diabetic ketoacidosis (euDKA)."
        )
    },
    {
        "id": "t2dm_med_glp1_07",
        "topic": "Medication Information",
        "title": "GLP-1 Receptor Agonists (Semaglutide, Dulaglutide, Liraglutide) in T2DM",
        "source": "ADA Standards of Care & DailyMed",
        "version": "2024",
        "section": "Pharmacologic Approaches to Glycemic Treatment",
        "citation": "ADA Standards of Care in Diabetes—2024, Section 9 & 10; DailyMed Semaglutide Prescribing Information",
        "content": (
            "Glucagon-like peptide-1 receptor agonists (GLP-1 RAs) enhance glucose-dependent insulin secretion, suppress inappropriate glucagon secretion, "
            "slow gastric emptying, and promote satiety via central nervous system pathways. "
            "Substantial HbA1c reduction (1.0% to 2.0%) and robust weight loss (5% to 15%). "
            "Cardiovascular outcome trials demonstrate significant reduction in 3-point MACE (cardiovascular death, non-fatal MI, non-fatal stroke) "
            "in patients with established ASCVD or high risk. "
            "Adverse effects are predominantly gastrointestinal (nausea, vomiting, diarrhea, constipation), which attenuate over time. "
            "Black box warning: contraindicated in patients with personal or family history of medullary thyroid carcinoma (MTC) or Multiple Endocrine Neoplasia syndrome type 2 (MEN 2). "
            "Caution is advised in patients with pre-existing severe proliferative diabetic retinopathy or history of pancreatitis."
        )
    },
    {
        "id": "t2dm_med_dpp4_su_08",
        "topic": "Medication Information",
        "title": "DPP-4 Inhibitors and Sulfonylureas in Type 2 Diabetes",
        "source": "ICMR Guidelines & DailyMed",
        "version": "2023-2024",
        "section": "Oral Antidiabetic Agents",
        "citation": "ICMR Guidelines for Management of T2DM 2023; DailyMed Sitagliptin and Glimepiride Prescribing Info",
        "content": (
            "Dipeptidyl peptidase-4 (DPP-4) inhibitors (Sitagliptin, Linagliptin, Vildagliptin) prevent degradation of endogenous incretin hormones (GLP-1, GIP). "
            "Efficacy: modest HbA1c reduction (0.5%–0.8%). Well-tolerated, weight-neutral, negligible hypoglycemia risk as monotherapy. "
            "Linagliptin requires no renal dose adjustment; Sitagliptin requires dose adjustment according to eGFR. "
            "Sulfonylureas (Glimepiride, Glipizide, Gliclazide) stimulate beta-cell insulin secretion by closing ATP-sensitive potassium channels. "
            "Efficacy: rapid initial HbA1c reduction (1.0%–1.5%), but lack durability due to progressive beta-cell failure. "
            "Major limitations: substantial hypoglycemia risk (especially in elderly patients or kidney impairment) and modest weight gain (1.5–2.5 kg). "
            "Sulfonylureas should not be combined with meglitinides, and caution is mandatory when combining with insulin."
        )
    },
    {
        "id": "t2dm_med_safety_09",
        "topic": "Medication Safety Information",
        "title": "Renal Dosing Adjustments and Medication Safety Thresholds in T2DM",
        "source": "ADA Standards of Care & DailyMed",
        "version": "2024",
        "section": "Safety, Renal Dosing, and Drug-Drug Interactions",
        "citation": "ADA Standards 2024, Section 11 (Chronic Kidney Disease); DailyMed Prescribing Alerts",
        "content": (
            "Critical renal safety thresholds for antidiabetic medications: "
            "1. Metformin: Measure eGFR prior to initiation. Safe to start if eGFR >= 45 mL/min/1.73m2. "
            "If eGFR is 30–44 mL/min/1.73m2, do not initiate; if already taking, max dose is 1000 mg/day with frequent renal monitoring. "
            "Contraindicated if eGFR < 30 mL/min/1.73m2 due to risk of lactic acidosis. Withhold prior to iodinated radiocontrast procedures in patients with eGFR 30-60. "
            "2. SGLT2 Inhibitors: Glycemic lowering declines below eGFR 45; can be continued for cardiorenal protection down to eGFR 20 mL/min/1.73m2 or dialysis. "
            "3. GLP-1 RAs: Dulaglutide and subcutaneous Semaglutide do not require dose adjustment for renal impairment, but hydration must be maintained to prevent acute kidney injury from GI volume depletion. "
            "4. Sulfonylureas: Prolonged half-life in renal impairment increases hypoglycemia risk; Glimepiride and Glyburide active metabolites accumulate; dose reduction or discontinuation required when eGFR < 45."
        )
    },
    {
        "id": "t2dm_adherence_10",
        "topic": "Medication Adherence",
        "title": "Adherence Evaluation, Clinical Inertia, and Behavioral Barriers",
        "source": "WHO & ADA Standards of Care",
        "version": "2023-2024",
        "section": "Facilitating Positive Health Behaviors and Well-being",
        "citation": "WHO Adherence to Long-Term Therapies: Evidence for Action; ADA Standards 2024, Section 5",
        "content": (
            "Medication adherence in chronic Type 2 Diabetes is a critical determinant of glycemic stability and complication prevention. "
            "Non-adherence rates reach 30%–50% in long-term observational cohorts, contributing to pseudo-refractory hyperglycemia. "
            "Key barriers include: complex multi-dose schedules, gastrointestinal adverse effects (metformin, GLP-1 RAs), fear of hypoglycemia (insulin, sulfonylureas), "
            "medication cost, and health literacy limitations. "
            "Dataset considerations: Publicly available retrospective datasets typically record refill encounters or self-report proxies rather than electronic pill-bottle monitoring. "
            "Proportion of Days Covered (PDC) >= 80% is the accepted benchmark for adequate adherence when prescription refill claims are available. "
            "When refill intervals are incomplete, metrics must be classified as proxy or exploratory indicators rather than validated ground-truth adherence."
        )
    },
    {
        "id": "t2dm_lifestyle_11",
        "topic": "Lifestyle Guidance",
        "title": "Medical Nutrition Therapy and Physical Activity for Type 2 Diabetes",
        "source": "ADA Standards of Care & ICMR Guidelines",
        "version": "2023-2024",
        "section": "Lifestyle Management",
        "citation": "ADA Standards of Care 2024, Section 5; ICMR T2DM Guidelines 2023, Ch. 2",
        "content": (
            "Lifestyle interventions form the cornerstone of T2DM management alongside pharmacotherapy: "
            "1. Nutrition: Emphasize nutrient-dense, high-fiber eating patterns (Mediterranean, DASH, plant-forward diets). "
            "Reduce refined carbohydrates, sugar-sweetened beverages, and ultra-processed foods. Focus on consistent carbohydrate distribution. "
            "2. Weight Management: A 5%–10% intentional weight reduction in overweight or obese patients produces clinically meaningful improvements in glycemic control, lipid profiles, and blood pressure. "
            "3. Physical Activity: Non-pregnant adults should engage in at least 150 minutes of moderate-to-vigorous aerobic activity weekly spread over at least 3 days, with no more than 2 consecutive days without exercise. "
            "Add 2–3 sessions of resistance exercise per week on non-consecutive days. "
            "4. Sleep & Behavioral Health: Encourage 7–8 hours of uninterrupted sleep; screen for obstructive sleep apnea and diabetes distress."
        )
    },
    {
        "id": "t2dm_complications_12",
        "topic": "Diabetes Complications",
        "title": "Microvascular and Macrovascular Complication Screening in T2DM",
        "source": "ADA Standards of Care",
        "version": "2024",
        "section": "Chronic Complications and Comorbidities",
        "citation": "ADA Standards of Care in Diabetes—2024, Section 11 & 12",
        "content": (
            "Screening guidelines for T2DM chronic complications: "
            "1. Retinopathy: Dilated, comprehensive eye examination by an ophthalmologist or optometrist at the time of T2DM diagnosis and annually thereafter (or every 2 years if exams are normal). "
            "2. Diabetic Kidney Disease: Annual assessment of urinary albumin-to-creatinine ratio (UACR) and eGFR beginning at diagnosis. "
            "3. Neuropathy: Annual screening for distal symmetric polyneuropathy using 10-g monofilament test, pinprick or temperature sensation, and ankle reflex testing. "
            "4. Diabetic Foot: Comprehensive foot examination annually to identify ulceration, peripheral arterial disease, and loss of protective sensation. "
            "5. Cardiovascular Disease: Regular assessment of cardiovascular risk factors (blood pressure >= 130/80 mmHg, dyslipidemia, smoking status, family history). ASCVD is the leading cause of morbidity and mortality."
        )
    },
    {
        "id": "t2dm_kidney_13",
        "topic": "Kidney Function Monitoring",
        "title": "Chronic Kidney Disease Staging, eGFR, and Albuminuria in T2DM",
        "source": "KDIGO 2023 Clinical Practice Guideline & ADA Standards",
        "version": "2023-2024",
        "section": "Kidney Disease and Risk Management",
        "citation": "KDIGO 2023 Diabetes Management in CKD; ADA Standards 2024, Section 11",
        "content": (
            "Diabetic Kidney Disease (DKD) is staged based on estimated Glomerular Filtration Rate (eGFR) and Urinary Albumin-to-Creatinine Ratio (UACR): "
            "eGFR Categories (mL/min/1.73m2): "
            "- G1: >= 90 (Normal or high) "
            "- G2: 60–89 (Mildly decreased) "
            "- G3a: 45–59 (Mildly to moderately decreased) "
            "- G3b: 30–44 (Moderately to severely decreased) "
            "- G4: 15–29 (Severely decreased) "
            "- G5: < 15 (Kidney failure) "
            "Albuminuria Categories (UACR in mg/g): "
            "- A1: < 30 (Normal to mildly increased) "
            "- A2: 30–300 (Moderately increased, microalbuminuria) "
            "- A3: > 300 (Severely increased, macroalbuminuria) "
            "First-line pharmacotherapy for T2DM with CKD (eGFR 20-60 or UACR >= 30) includes an SGLT2 inhibitor and an ACE inhibitor or ARB (titrated to maximum tolerated dose). "
            "Nonsteroidal mineralocorticoid receptor antagonist (Finerenone) is recommended for persistent albuminuria."
        )
    },
    {
        "id": "t2dm_lipids_14",
        "topic": "Lipid Profile Monitoring",
        "title": "Dyslipidemia Management and Cardiovascular Risk Reduction in T2DM",
        "source": "ADA Standards of Care",
        "version": "2024",
        "section": "Cardiovascular Disease and Risk Management",
        "citation": "ADA Standards of Care in Diabetes—2024, Section 10",
        "content": (
            "Dyslipidemia in T2DM is characteristically atherogenic: elevated plasma triglycerides, decreased HDL-C, and normal or mildly increased LDL-C "
            "consisting of small, dense LDL particles. "
            "Statin therapy guidelines: "
            "1. Primary prevention (Age 40–75 without ASCVD): Moderate-intensity statin therapy (e.g., Atorvastatin 20 mg, Rosuvastatin 10 mg) recommended. "
            "In patients with multiple ASCVD risk factors, high-intensity statin is recommended to achieve an LDL-C reduction of >= 50% from baseline and LDL-C target < 70 mg/dL. "
            "2. Secondary prevention (Established ASCVD): High-intensity statin therapy (Atorvastatin 40–80 mg, Rosuvastatin 20–40 mg) targeting LDL-C < 55 mg/dL. "
            "If LDL-C remains >= 55 mg/dL on maximally tolerated statin, add Ezetimibe or PCSK9 inhibitor. "
            "Hypertriglyceridemia (fasting triglycerides >= 500 mg/dL) necessitates dietary intervention and consideration of fibrates or icosapent ethyl to prevent pancreatitis."
        )
    },
    {
        "id": "t2dm_followup_15",
        "topic": "Follow-up and Monitoring Recommendations",
        "title": "Clinical Follow-up Intervals and Decision Support Principles",
        "source": "ADA Standards of Care & WHO",
        "version": "2024",
        "section": "Comprehensive Clinical Review Schedule",
        "citation": "ADA Standards 2024, Section 4; WHO Package of Essential NCD Interventions 2023",
        "content": (
            "Clinical visit frequency: Patients meeting treatment goals should be evaluated every 6 months. "
            "Patients not meeting treatment goals, or experiencing therapy modifications, adverse effects, or frequent hypoglycemia, should be reviewed every 3 months or sooner. "
            "Every clinical encounter must evaluate: "
            "1. Glycemic trends (HbA1c, fasting/postprandial records). "
            "2. Medication tolerance, reported adherence barriers, and adverse reactions. "
            "3. Blood pressure measurement (target < 130/80 mmHg). "
            "4. Symptomatic assessment of hypoglycemia, neuropathy, and volume status. "
            "Decision support rule: Clinical AI tools serve strictly as diagnostic and management aids for clinician review. "
            "All recommendations must present observed longitudinal evidence alongside guideline citations, without autonomous prescribing or dosing alterations."
        )
    },
     {
        "id": "t2dm_dm_metformin_safety_31",
        "topic": "Medication Safety Information",
        "title": "Metformin Boxed Warning, Contraindications, and Drug Interactions",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Boxed Warning; Contraindications; Drug Interactions",
        "citation": "DailyMed Metformin Hydrochloride Tablets Prescribing Information",
        "content": (
            "Metformin carries a boxed warning for lactic acidosis. Risk factors include renal impairment, age >= 65, radiological studies with contrast, "
            "surgery and other procedures, hypoxic states (acute congestive heart failure), excessive alcohol intake, and hepatic impairment. "
            "Contraindications: eGFR < 30 mL/min/1.73m2, acute or chronic metabolic acidosis including diabetic ketoacidosis, and known hypersensitivity. "
            "Initiation is not recommended at eGFR 30-45. Interacting drugs that can raise metformin exposure or lactic acidosis risk include carbonic anhydrase inhibitors "
            "(topiramate, zonisamide, acetazolamide), cationic drugs that compete for renal tubular secretion (cimetidine, dolutegravir, ranolazine, vandetanib), "
            "and alcohol. Metformin should be temporarily stopped at or before iodinated contrast imaging in patients with eGFR 30-60, hepatic disease, "
            "alcoholism, or heart failure, and eGFR re-evaluated 48 hours afterward."
        )
    },
    {
        "id": "t2dm_dm_pioglitazone_32",
        "topic": "Medication Information",
        "title": "Pioglitazone (Thiazolidinedione) Efficacy, Dosing, and Warnings",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Boxed Warning; Warnings and Precautions",
        "citation": "DailyMed Pioglitazone Tablets Prescribing Information",
        "content": (
            "Pioglitazone is a PPAR-gamma agonist that improves insulin sensitivity in adipose tissue, muscle, and liver. "
            "The usual starting dose is 15 mg or 30 mg once daily, with a maximum of 45 mg once daily. "
            "Boxed warning: thiazolidinediones cause or exacerbate congestive heart failure. It is not recommended in symptomatic heart failure and is "
            "contraindicated in NYHA Class III or IV heart failure. Other warnings include fluid retention and edema, weight gain, bone fracture risk (mainly in women), "
            "macular edema, hepatic effects (check liver tests at baseline), and bladder cancer (should not be used in patients with active bladder cancer; "
            "use caution in those with prior bladder cancer history). Hypoglycemia risk is low as monotherapy but increases with insulin or secretagogues. "
            "Strong CYP2C8 inhibitors such as gemfibrozil raise exposure, and the dose should be limited to 15 mg daily with concomitant gemfibrozil."
        )
    },
    {
        "id": "t2dm_dm_glp1_dosing_33",
        "topic": "Medication Information",
        "title": "Semaglutide and Dulaglutide Dosing Schedules and Administration",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration",
        "citation": "DailyMed Semaglutide Injection and Oral Semaglutide Tablets Prescribing Information; DailyMed Dulaglutide Prescribing Information",
        "content": (
            "Subcutaneous semaglutide (once weekly): start 0.25 mg weekly for 4 weeks (initiation dose, not intended for glycemic control), "
            "then 0.5 mg weekly; if additional control is needed, increase to 1 mg after at least 4 weeks, then to 2 mg after at least 4 more weeks. "
            "Oral semaglutide (once daily): start 3 mg for 30 days, then 7 mg; may increase to 14 mg after at least 30 days. "
            "It must be taken on an empty stomach with no more than 4 ounces of plain water, at least 30 minutes before the first food, beverage, or other oral medicines. "
            "Dulaglutide (once weekly): 0.75 mg weekly, may increase to 1.5 mg after at least 4 weeks, and further to 3 mg and 4.5 mg at intervals of at least 4 weeks. "
            "A missed weekly dose can be given within 5 days of the missed dose for semaglutide injection; otherwise skip and resume the regular schedule."
        )
    },
    {
        "id": "t2dm_dm_tirzepatide_34",
        "topic": "Medication Information",
        "title": "Tirzepatide Dual GIP/GLP-1 Receptor Agonist: Dosing and Safety",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Boxed Warning; Drug Interactions",
        "citation": "DailyMed Tirzepatide Injection Prescribing Information",
        "content": (
            "Tirzepatide is a once-weekly subcutaneous dual GIP and GLP-1 receptor agonist. The starting dose is 2.5 mg weekly for 4 weeks (for treatment initiation), "
            "then 5 mg weekly. Doses may be increased in 2.5 mg steps after at least 4 weeks on the current dose, up to a maximum of 15 mg weekly. "
            "Boxed warning: risk of thyroid C-cell tumors; contraindicated with personal or family history of medullary thyroid carcinoma or MEN 2. "
            "Warnings include pancreatitis, gallbladder disease, acute kidney injury from volume depletion, diabetic retinopathy complications, and hypoglycemia when combined "
            "with insulin or sulfonylureas (consider reducing their doses). Tirzepatide delays gastric emptying and may reduce the efficacy of oral hormonal contraceptives; "
            "patients using them should switch to a non-oral method or add a barrier method for 4 weeks after initiation and after each dose escalation. "
            "Common adverse reactions are nausea, diarrhea, decreased appetite, vomiting, and constipation."
        )
    },
    {
        "id": "t2dm_dm_sglt2_safety_35",
        "topic": "Medication Safety Information",
        "title": "SGLT2 Inhibitor Warnings: Ketoacidosis, Perioperative Holding, and Genital Infections",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Warnings and Precautions",
        "citation": "DailyMed Empagliflozin, Dapagliflozin, Canagliflozin, and Ertugliflozin Prescribing Information",
        "content": (
            "Ketoacidosis has been reported with SGLT2 inhibitors in type 1 and type 2 diabetes, sometimes with near-normal glucose (euglycemic DKA). "
            "Risk factors: insulin dose reduction, acute illness, reduced food or fluid intake, surgery, and alcohol abuse. "
            "Consider temporarily discontinuing at least 3 days before scheduled surgery (at least 4 days for ertugliflozin). "
            "Other warnings: volume depletion and hypotension (particularly with loop diuretics, older age, or low systolic blood pressure), urosepsis and pyelonephritis, "
            "necrotizing fasciitis of the perineum (Fournier's gangrene), genital mycotic infections, and hypoglycemia when used with insulin or secretagogues. "
            "Lower limb amputation risk was highlighted for canagliflozin in earlier trials; foot care monitoring is advised. "
            "Contraindicated in patients on dialysis for the glycemic indication and in those with hypersensitivity to the drug."
        )
    },
    {
        "id": "t2dm_dm_dpp4_dosing_36",
        "topic": "Medication Information",
        "title": "DPP-4 Inhibitor Renal Dosing and Safety Warnings",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Warnings and Precautions",
        "citation": "DailyMed Sitagliptin, Linagliptin, Saxagliptin, and Alogliptin Prescribing Information",
        "content": (
            "Sitagliptin usual dose is 100 mg once daily with eGFR >= 45; 50 mg once daily with eGFR 30 to < 45; 25 mg once daily with eGFR < 30 or on dialysis. "
            "Linagliptin 5 mg once daily requires no renal dose adjustment (primarily non-renal elimination). "
            "Saxagliptin 5 mg daily (2.5 mg if eGFR <= 45 or with strong CYP3A4/5 inhibitors); alogliptin dose is reduced at eGFR < 60. "
            "Warnings across the class: acute pancreatitis (discontinue if suspected), heart failure risk with saxagliptin and alogliptin (consider risks in patients "
            "with heart failure or renal impairment), severe and disabling arthralgia, bullous pemphigoid, and hypersensitivity reactions including angioedema. "
            "DPP-4 inhibitors should not be combined with a GLP-1 receptor agonist because of no additional benefit."
        )
    },
    {
        "id": "t2dm_dm_su_meglitinide_37",
        "topic": "Medication Information",
        "title": "Sulfonylurea and Meglitinide Dosing, Interactions, and Hypoglycemia Risk",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Drug Interactions",
        "citation": "DailyMed Glimepiride, Glipizide, Gliclazide (where marketed), Repaglinide, and Nateglinide Prescribing Information",
        "content": (
            "Glimepiride is started at 1-2 mg once daily with breakfast and titrated to a maximum of 8 mg daily; start at 1 mg in renal impairment or in elderly patients. "
            "Glipizide immediate release is started at 5 mg before breakfast (2.5 mg in elderly or hepatic disease), maximum 40 mg/day. "
            "Sulfonylureas should be used cautiously with sulfonamide allergy, G6PD deficiency (hemolysis risk), and concomitant drugs that potentiate hypoglycemia "
            "(fluoroquinolones, beta-blockers, salicylates, fluconazole). "
            "Repaglinide 0.5-4 mg and nateglinide 120 mg are taken 0-30 minutes before meals; skip the dose if the meal is skipped. "
            "Repaglinide is contraindicated with gemfibrozil because of markedly increased repaglinide exposure and prolonged hypoglycemia. "
            "Hypoglycemia is the principal adverse effect of both classes and weight gain is common."
        )
    },
    {
        "id": "t2dm_dm_agi_38",
        "topic": "Medication Information",
        "title": "Acarbose (Alpha-Glucosidase Inhibitor) Use and Precautions",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Contraindications",
        "citation": "DailyMed Acarbose Tablets Prescribing Information",
        "content": (
            "Acarbose inhibits intestinal alpha-glucosidase enzymes and delays carbohydrate digestion, mainly lowering postprandial glucose. "
            "Start at 25 mg three times daily with the first bite of each main meal; titrate at 4-8 week intervals to a maximum of 100 mg three times daily "
            "(50 mg three times daily for patients weighing 60 kg or less). Typical HbA1c reduction is about 0.5-0.8%. "
            "Common adverse effects are flatulence, diarrhea, and abdominal pain, which improve with slow titration. "
            "Contraindications: diabetic ketoacidosis, cirrhosis, inflammatory bowel disease, colonic ulceration, partial intestinal obstruction, "
            "and conditions predisposing to intestinal obstruction or chronic intestinal disease with malabsorption. "
            "Acarbose alone does not cause hypoglycemia, but when it occurs with other agents it must be treated with oral glucose (dextrose), not sucrose, "
            "because sucrose breakdown is delayed."
        )
    },
    {
        "id": "t2dm_dm_insulin_pk_39",
        "topic": "Insulin Therapy",
        "title": "Insulin Product Pharmacokinetic Profiles (Onset, Peak, Duration)",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Clinical Pharmacology",
        "citation": "DailyMed Prescribing Information for Insulin Lispro, Aspart, Regular Human Insulin, NPH, Glargine, Detemir, and Degludec",
        "content": (
            "Approximate pharmacokinetic profiles after subcutaneous injection (individual variability is substantial): "
            "Rapid-acting analogs (lispro, aspart, glulisine): onset 10-20 minutes, peak 1-3 hours, duration 3-5 hours; given 0-15 minutes before meals. "
            "Regular human insulin: onset 30-60 minutes, peak 2-4 hours, duration 5-8 hours; given about 30 minutes before meals. "
            "NPH insulin: onset 1-2 hours, peak 4-10 hours, duration 10-18 hours. "
            "Long-acting analogs: glargine U-100 provides roughly 24 hours of action with no pronounced peak; glargine U-300 up to 36 hours; "
            "detemir about 12-24 hours depending on dose; degludec longer than 42 hours with a flat profile, allowing flexible dosing times. "
            "Insulin must never be shared between patients, and injection sites should be rotated to reduce lipohypertrophy. "
            "Insulin requirements can fall in renal impairment because of reduced insulin clearance."
        )
    },
    {
        "id": "t2dm_dm_statin_safety_40",
        "topic": "Lipid Profile Monitoring",
        "title": "Statin Prescribing Information: Myopathy, Interactions, and Renal/Asian Dosing",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Warnings and Precautions; Drug Interactions",
        "citation": "DailyMed Atorvastatin Calcium Tablets and Rosuvastatin Calcium Tablets Prescribing Information",
        "content": (
            "Atorvastatin dose range is 10-80 mg once daily (any time of day); high-intensity is 40-80 mg. "
            "Rosuvastatin dose range is 5-40 mg once daily; high-intensity is 20-40 mg. Rosuvastatin exposure is approximately twofold higher in Asian patients, "
            "so the label recommends considering a 5 mg starting dose. In severe renal impairment (CrCl < 30 mL/min/1.73m2) not on hemodialysis, "
            "start rosuvastatin at 5 mg with a maximum of 10 mg daily. "
            "Warnings: myopathy and rhabdomyolysis (risk raised by age >= 65, hypothyroidism, renal impairment, and interacting drugs), immune-mediated necrotizing myopathy, "
            "and hepatic enzyme elevations (check liver enzymes at baseline when clinically indicated). "
            "Interactions: gemfibrozil, cyclosporine, and certain protease inhibitors increase statin exposure; atorvastatin has limits with clarithromycin, itraconazole, and others. "
            "Statins may slightly raise HbA1c and fasting glucose, but cardiovascular benefit generally outweighs this risk in diabetes."
        )
    },
    {
        "id": "t2dm_dm_acei_arb_41",
        "topic": "Hypertension",
        "title": "ACE Inhibitor and ARB Prescribing Information: Boxed Warning and Monitoring",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Boxed Warning; Warnings and Precautions",
        "citation": "DailyMed Lisinopril, Enalapril, Losartan, and Telmisartan Prescribing Information",
        "content": (
            "ACE inhibitors and ARBs carry a boxed warning for fetal toxicity: discontinue as soon as pregnancy is detected, because drugs acting on the renin-angiotensin system "
            "can cause injury and death to the developing fetus. Other warnings: angioedema (more frequent with ACE inhibitors and in Black patients; contraindicated with a history "
            "of ACE-inhibitor-related angioedema), hypotension (volume depletion), hyperkalemia, and renal function deterioration, particularly in bilateral renal artery stenosis "
            "or stenosis of a solitary kidney. ACE inhibitors cause a persistent dry cough in a subset of patients; an ARB is a common alternative. "
            "Dual blockade with ACE inhibitor plus ARB, or with aliskiren in patients with diabetes, is contraindicated or not recommended because of increased hyperkalemia, hypotension, and renal failure. "
            "Check serum creatinine and potassium before and 1-2 weeks after starting or changing dose. NSAIDs can blunt the antihypertensive effect and worsen renal function."
        )
    },
    {
        "id": "t2dm_dm_finerenone_42",
        "topic": "Kidney Function Monitoring",
        "title": "Finerenone Dosing, Potassium Monitoring, and Interactions in Diabetic Kidney Disease",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Contraindications; Warnings and Precautions",
        "citation": "DailyMed Finerenone Tablets Prescribing Information",
        "content": (
            "Finerenone is a nonsteroidal mineralocorticoid receptor antagonist indicated to reduce the risk of sustained eGFR decline, end-stage kidney disease, "
            "cardiovascular death, non-fatal myocardial infarction, and hospitalization for heart failure in adults with CKD associated with T2DM. "
            "Before starting, check serum potassium and eGFR: do not initiate if potassium is > 5.0 mEq/L. "
            "Starting dose is 10 mg once daily if eGFR is 25 to < 60 mL/min/1.73m2, and 20 mg once daily if eGFR >= 60. "
            "Measure potassium and eGFR 4 weeks after initiation or dose change and periodically thereafter; the dose may be increased to 20 mg when potassium is <= 4.8 mEq/L. "
            "Contraindications: concomitant strong CYP3A4 inhibitors (itraconazole, clarithromycin, ketoconazole) and adrenal insufficiency (Addison's disease). "
            "Avoid grapefruit juice and moderate CYP3A4 inhibitors where possible; hyperkalemia is the key adverse effect."
        )
    },
    {
        "id": "t2dm_dm_glucagon_43",
        "topic": "Hypoglycemia",
        "title": "Glucagon Products for Severe Hypoglycemia: Use and Administration",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Dosage and Administration; Warnings and Precautions",
        "citation": "DailyMed Glucagon for Injection, Glucagon Injection (prefilled), and Nasal Glucagon Prescribing Information",
        "content": (
            "Glucagon is indicated for treatment of severe hypoglycemia in patients with diabetes. Standard adult dose by injection (subcutaneous, intramuscular, or intravenous "
            "in a supervised setting) is 1 mg; nasal glucagon is a single 3 mg dose in one nostril, which does not require inhalation. "
            "After administration the patient should be turned onto their side to reduce aspiration risk, and emergency medical services should be called. "
            "If the patient does not respond within 15 minutes, a further dose from a new device can be given while awaiting help. Once awake and able to swallow, "
            "give oral fast-acting carbohydrate followed by longer-acting carbohydrate and a protein-containing snack to prevent recurrence. "
            "Glucagon may be less effective in patients with depleted hepatic glycogen (prolonged fasting, adrenal insufficiency, chronic hypoglycemia, heavy alcohol use). "
            "Contraindicated in pheochromocytoma and insulinoma."
        )
    },
    {
        "id": "t2dm_dm_interactions_44",
        "topic": "Medication Safety Information",
        "title": "Drugs That Commonly Affect Glycemic Control in Patients with T2DM",
        "source": _SRC,
        "version": "Current label at time of writing",
        "section": "Drug Interactions",
        "citation": "DailyMed Prescribing Information for Prednisone, Thiazide Diuretics, Beta-blockers, Atypical Antipsychotics, and Fluoroquinolones",
        "content": (
            "Medications that can raise blood glucose include systemic corticosteroids (dose-related postprandial hyperglycemia, typically afternoon and evening), thiazide and loop diuretics, "
            "atypical antipsychotics (olanzapine, clozapine), protease inhibitors, niacin at high doses, and some immunosuppressants (tacrolimus, cyclosporine). "
            "Medications that can potentiate hypoglycemia include fluoroquinolones (both hypoglycemia and hyperglycemia reported, particularly in older adults on sulfonylureas or insulin), "
            "salicylates, sulfonamides, and ACE inhibitors in some patients. Non-selective beta-blockers can mask adrenergic warning symptoms of hypoglycemia such as palpitations and tremor, "
            "although sweating is preserved. Alcohol can cause delayed hypoglycemia, particularly with insulin or sulfonylureas. "
            "Medication reconciliation at each visit should include over-the-counter and herbal products."
        )
    },
    {
"id": "t2dm_ada_a1c_eag_45",
"topic": "HbA1c Interpretation",
"title": "HbA1c, Estimated Average Glucose, and Glucose Management Indicator",
"source": _SRC1,
"version": "2024",
"section": "Glycemic Goals and Hypoglycemia: Assessment of Glycemic Control",
"citation": "ADA Standards of Care in Diabetes-2024, Section 6",
"content": (
"HbA1c correlates with estimated average glucose (eAG) by the formula eAG (mg/dL) = 28.7 x HbA1c - 46.7. "
"Approximate equivalents: HbA1c 6% = 126 mg/dL; 7% = 154 mg/dL; 8% = 183 mg/dL; 9% = 212 mg/dL; 10% = 240 mg/dL. "
"The Glucose Management Indicator (GMI) is calculated from CGM mean glucose: GMI (%) = 3.31 + 0.02392 x mean glucose (mg/dL). "
"GMI and laboratory HbA1c can differ by 0.5% or more in many individuals because of variation in red cell lifespan and glycation; "
"when they are discordant, CGM or SMBG data should guide decisions. "
"HbA1c should be measured at least twice per year in people meeting goals with stable control and quarterly when therapy has changed or goals are unmet. "
"Point-of-care HbA1c is appropriate only with an assay that is NGSP-certified and FDA-cleared for the setting."
)
},
{
"id": "t2dm_ada_hba1c_limits_46",
"topic": "HbA1c Interpretation",
"title": "Conditions That Make HbA1c Unreliable",
"source": _SRC1,
"version": "2024",
"section": "Glycemic Goals and Hypoglycemia: Assessment of Glycemic Control",
"citation": "ADA Standards of Care in Diabetes-2024, Section 2 and Section 6",
"content": (
"HbA1c can be falsely low when red cell turnover is increased: hemolytic anemia, recent blood loss or transfusion, erythropoietin therapy, "
"and pregnancy (second and third trimesters). It can be falsely high with iron deficiency anemia, vitamin B12 or folate deficiency, "
"and reduced red cell turnover. Hemoglobin variants (for example HbS, HbC, HbE, and HbD traits) may interfere depending on the assay; "
"the laboratory should use a method without interference or the clinician should rely on glucose-based measures. "
"In end-stage kidney disease, HbA1c is less reliable; glycated albumin, fructosamine, or CGM data are alternatives. "
"Fructosamine reflects glycemia over about 2-3 weeks."
)
},
{
"id": "t2dm_ada_smbg_47",
"topic": "Blood Glucose Measurements",
"title": "Self-Monitoring of Blood Glucose: Indications and Use",
"source": _SRC1,
"version": "2024",
"section": "Diabetes Technology: Self-Monitoring of Blood Glucose",
"citation": "ADA Standards of Care in Diabetes-2024, Section 7",
"content": (
"SMBG should be offered to all people on insulin and considered for those on other therapies when it informs behavior or treatment decisions. "
"People on multiple daily insulin injections should check glucose before meals and snacks, at bedtime, occasionally after meals, "
"before exercise, when they suspect hypoglycemia, after treating hypoglycemia until normal, and before critical tasks such as driving. "
"For people on basal insulin only, fasting checks guide titration. For those on non-insulin therapies with low hypoglycemia risk, "
"structured, intermittent testing (for example paired pre- and post-meal readings) can support education. "
"Meter accuracy, technique (clean hands, adequate sample), strip storage, and expiry dates should be reviewed periodically."
)
},
{
"id": "t2dm_ada_alg_cardiorenal_48",
"topic": "Medication Information",
"title": "Pharmacologic Approach: Comorbidity-Driven Choice of Glucose-Lowering Agents",
"source": _SRC1,
"version": "2024",
"section": "Pharmacologic Approaches to Glycemic Treatment",
"citation": "ADA Standards of Care in Diabetes-2024, Section 9, Figure 9.3",
"content": (
"Treatment selection is person-centered and should address comorbidities, hypoglycemia risk, weight, cost, and patient preference. "
"For people with established ASCVD or high cardiovascular risk, a GLP-1 receptor agonist or SGLT2 inhibitor with proven cardiovascular benefit is recommended "
"independent of baseline HbA1c and of metformin use. For heart failure (especially HFrEF) or CKD with eGFR 20-60 or albuminuria, "
"an SGLT2 inhibitor is recommended; a GLP-1 RA with proven benefit is an alternative when an SGLT2 inhibitor is not tolerated or contraindicated. "
"For CKD with albuminuria, finerenone is added to an ACE inhibitor or ARB when appropriate. "
"Metformin remains an effective, inexpensive option for glycemic management but is no longer required as the first step when these conditions are present."
)
},
{
"id": "t2dm_ada_alg_goals_49",
"topic": "Medication Information",
"title": "Pharmacologic Approach: Weight and Hypoglycemia Goals, Relative Glucose-Lowering Efficacy",
"source": _SRC1,
"version": "2024",
"section": "Pharmacologic Approaches to Glycemic Treatment",
"citation": "ADA Standards of Care in Diabetes-2024, Section 9, Figure 9.3 and Table 9.2",
"content": (
"When weight management is a goal, agents with very high weight-loss efficacy (semaglutide, tirzepatide) are preferred, followed by those with high efficacy "
"(dulaglutide, liraglutide). SGLT2 inhibitors and metformin have intermediate or neutral effects; DPP-4 inhibitors are weight-neutral; "
"sulfonylureas, insulin, and pioglitazone cause weight gain. "
"When avoiding hypoglycemia is a priority, agents with low risk include metformin, GLP-1 RAs, SGLT2 inhibitors, DPP-4 inhibitors, and thiazolidinediones. "
"Glucose-lowering efficacy is described as very high for dulaglutide (high dose), semaglutide, tirzepatide, insulin, and combination oral therapy; "
"high for other GLP-1 RAs, metformin, SGLT2 inhibitors (intermediate in some tables), sulfonylureas, and thiazolidinediones; "
"and intermediate for DPP-4 inhibitors."
)
},
{
"id": "t2dm_ada_alg_intensify_50",
"topic": "Medication Information",
"title": "Treatment Intensification, Combination Therapy, and Avoiding Clinical Inertia",
"source": _SRC1,
"version": "2024",
"section": "Pharmacologic Approaches to Glycemic Treatment",
"citation": "ADA Standards of Care in Diabetes-2024, Section 9",
"content": (
"Treatment should be reassessed every 3-6 months and modified if glycemic, weight, or other goals are not met; delays in intensification (clinical inertia) "
"are a major contributor to poor outcomes. Early combination therapy can be considered at diagnosis to extend the time to treatment failure, "
"particularly when HbA1c is 1.5% or more above the individualized goal. "
"Insulin should be considered regardless of background therapy when there is evidence of ongoing catabolism (weight loss), symptoms of hyperglycemia, "
"HbA1c above 10%, or blood glucose >= 300 mg/dL. Once insulin is started, GLP-1 RA combination is preferred over escalating insulin alone. "
"Therapy should be de-intensified when it is causing hypoglycemia or when goals are overly stringent for the individual's health status. "
"Cost, access, and insurance coverage should be discussed openly."
)
},
{
"id": "t2dm_ada_dsmes_51",
"topic": "Patient Education",
"title": "Diabetes Self-Management Education and Support (DSMES) and Nutrition Therapy",
"source": _SRC1,
"version": "2024",
"section": "Facilitating Positive Health Behaviors and Well-being",
"citation": "ADA Standards of Care in Diabetes-2024, Section 5",
"content": (
"DSMES should be offered at four critical times: at diagnosis, annually and/or when not meeting treatment targets, when complicating factors develop, "
"and when transitions in life or care occur. DSMES improves HbA1c, lowers cost, and reduces hospital admissions. "
"Medical nutrition therapy delivered by a registered dietitian improves HbA1c by approximately 1.0-1.9% in T2DM. "
"There is no single ideal macronutrient distribution; eating patterns should be individualized (Mediterranean, DASH, plant-based, or lower-carbohydrate patterns can all be effective). "
"Sugar-sweetened beverages should be replaced with water where possible, and sodium intake should be below 2,300 mg/day. "
"Smoking and e-cigarette cessation should be assessed and supported at every visit; alcohol intake should be limited (up to one drink per day for women and two for men) with awareness of hypoglycemia risk."
)
},
{
"id": "t2dm_ada_ckd_monitor_52",
"topic": "Kidney Function Monitoring",
"title": "CKD Screening Frequency, Risk Stratification, and Nephrology Referral",
"source": _SRC1,
"version": "2024",
"section": "Chronic Kidney Disease and Risk Management",
"citation": "ADA Standards of Care in Diabetes-2024, Section 11",
"content": (
"People with T2DM should have UACR and eGFR assessed at diagnosis and at least annually. An abnormal UACR (>= 30 mg/g) should be confirmed on two of three specimens "
"collected within 3-6 months because of variability (exercise, infection, fever, heart failure, marked hyperglycemia, and menstruation can transiently raise UACR). "
"Monitoring frequency increases with CKD risk categories from KDIGO (1-4 times yearly depending on eGFR and albuminuria). "
"Optimizing blood pressure and glycemic control, using SGLT2 inhibitors, and RAS inhibitors for albuminuria slows progression. "
"Referral to nephrology is advised for eGFR < 30, rapidly declining eGFR, persistent heavy albuminuria (UACR >= 300 mg/g) despite treatment, "
"refractory hyperkalemia or hypertension, signs suggesting a non-diabetic cause (active urine sediment, absent retinopathy in long-standing disease, rapid onset), "
"or difficulty managing complications."
)
},
{
"id": "t2dm_ada_retino_53",
"topic": "Diabetes Complications",
"title": "Diabetic Retinopathy: Screening, Risk Reduction, and Treatment",
"source": _SRC1,
"version": "2024",
"section": "Retinopathy, Neuropathy, and Foot Care",
"citation": "ADA Standards of Care in Diabetes-2024, Section 12",
"content": (
"Adults with T2DM should have an initial dilated and comprehensive eye examination at diagnosis, then every 1-2 years if no retinopathy and glycemia is well controlled; "
"annually or more often if any level of retinopathy is present. Retinal photography with remote reading or validated artificial intelligence systems "
"can serve as screening but does not replace a comprehensive exam. "
"Optimizing glycemia, blood pressure, and lipids reduces onset and progression. Rapid HbA1c lowering can transiently worsen retinopathy, "
"so patients with existing retinopathy starting intensive therapy (including semaglutide) should be monitored. "
"Treatment of center-involved diabetic macular edema and proliferative retinopathy includes intravitreal anti-VEGF agents and panretinal photocoagulation, "
"managed by an ophthalmologist. Fenofibrate may slow retinopathy progression in some patients."
)
},
{
"id": "t2dm_ada_neuropathy_54",
"topic": "Diabetes Complications",
"title": "Diabetic Peripheral and Autonomic Neuropathy: Diagnosis and Pain Management",
"source": _SRC1,
"version": "2024",
"section": "Retinopathy, Neuropathy, and Foot Care",
"citation": "ADA Standards of Care in Diabetes-2024, Section 12",
"content": (
"Distal symmetric polyneuropathy is a diagnosis of exclusion; other causes such as B12 deficiency (especially with metformin), hypothyroidism, alcohol, "
"renal disease, and medications should be assessed. Screening at diagnosis and annually uses the 10-g monofilament plus one other test (pinprick, temperature, "
"128-Hz vibration, or ankle reflexes). For neuropathic pain, first-line agents include gabapentinoids (pregabalin, gabapentin), SNRIs (duloxetine, venlafaxine), "
"tricyclic antidepressants, and sodium channel blockers; opioids including tapentadol are not recommended as first- or second-line therapy. "
"Autonomic neuropathy manifestations to screen for include resting tachycardia, orthostatic hypotension, gastroparesis, erectile dysfunction, and hypoglycemia unawareness. "
"Glycemic optimization prevents or delays neuropathy in T2DM but is less effective at reversing established nerve damage."
)
},
{
"id": "t2dm_ada_pregnancy_55",
"topic": "Special Populations",
"title": "Preexisting Diabetes in Pregnancy: Preconception Care, Targets, and Aspirin",
"source": _SRC1,
"version": "2024",
"section": "Management of Diabetes in Pregnancy",
"citation": "ADA Standards of Care in Diabetes-2024, Section 15",
"content": (
"Women of reproductive age with diabetes need preconception counseling, effective contraception until glycemia is optimized, and folic acid supplementation "
"(at least 400 micrograms daily) beginning before conception. Where safely achievable, the HbA1c goal in pregnancy is < 6% (and < 7% may be acceptable to avoid hypoglycemia). "
"Glucose targets: fasting < 95 mg/dL, 1-hour postprandial < 140 mg/dL, or 2-hour postprandial < 120 mg/dL. "
"Insulin is the preferred agent for most pregnancies with diabetes; metformin and glyburide cross the placenta and are not first-line. "
"ACE inhibitors, ARBs, and statins should be discontinued before or on recognition of pregnancy. "
"Low-dose aspirin (100-150 mg/day) is recommended starting at 12-16 weeks of gestation to reduce preeclampsia risk. "
"Retinopathy screening should occur before pregnancy or in the first trimester and be repeated as needed."
)
},
{
"id": "t2dm_ada_gdm_56",
"topic": "Special Populations",
"title": "Gestational Diabetes Mellitus: Screening and Diagnostic Thresholds",
"source": _SRC1,
"version": "2024",
"section": "Classification and Diagnosis of Diabetes: Gestational Diabetes Mellitus",
"citation": "ADA Standards of Care in Diabetes-2024, Section 2 and Section 15",
"content": (
"Gestational diabetes mellitus (GDM) is screened at 24-28 weeks of gestation in women not previously known to have diabetes; early testing is advised for women with risk factors. "
"One-step strategy: 75 g OGTT with thresholds fasting >= 92 mg/dL, 1-hour >= 180 mg/dL, 2-hour >= 153 mg/dL; one abnormal value is diagnostic. "
"Two-step strategy: 50 g non-fasting glucose challenge (threshold >= 130, 135, or 140 mg/dL at 1 hour), followed by a 100 g OGTT if positive, using Carpenter-Coustan thresholds "
"(fasting 95, 1-hour 180, 2-hour 155, 3-hour 140 mg/dL), with two or more abnormal values required. "
"Women with GDM should be screened for persistent diabetes or prediabetes at 4-12 weeks postpartum with a 75 g OGTT, "
"then every 1-3 years lifelong because of elevated T2DM risk."
)
},
{
"id": "t2dm_ada_hospital_57",
"topic": "Inpatient Care",
"title": "Inpatient Glycemic Management: Targets, Insulin, and Medications to Hold",
"source": _SRC1,
"version": "2024",
"section": "Diabetes Care in the Hospital",
"citation": "ADA Standards of Care in Diabetes-2024, Section 16",
"content": (
"Insulin therapy should be started for persistent hyperglycemia >= 180 mg/dL in hospitalized patients; the target range for most critically ill and non-critically ill patients is 140-180 mg/dL. "
"More stringent targets (110-140 mg/dL) may be appropriate for selected patients if achievable without significant hypoglycemia. "
"Basal insulin or basal plus correction insulin is preferred for non-critically ill patients; sole use of sliding-scale correction insulin is discouraged. "
"Intravenous insulin infusion is used in the ICU and for DKA/HHS. Metformin is generally held during hospitalization (contrast, acute kidney injury, hypoxia), "
"and SGLT2 inhibitors should be withheld during acute illness and before surgery. "
"Every inpatient with diabetes needs a hypoglycemia management protocol, and an HbA1c should be checked if not available within the previous 3 months. "
"Discharge planning should include medication reconciliation and follow-up within one month (or earlier when indicated)."
)
},
{
"id": "t2dm_ada_youth_58",
"topic": "Special Populations",
"title": "Youth-Onset Type 2 Diabetes: Diagnosis and Management Principles",
"source": _SRC1,
"version": "2024",
"section": "Children and Adolescents",
"citation": "ADA Standards of Care in Diabetes-2024, Section 14",
"content": (
"Youth with overweight or obesity (BMI >= 85th percentile) plus risk factors (family history, high-risk ethnicity, signs of insulin resistance such as acanthosis nigricans, "
"PCOS, or maternal GDM) should be screened beginning at age 10 or pubertal onset, whichever is earlier, and every 3 years thereafter. "
"Pediatric T2DM progresses faster than adult-onset disease, with earlier complications. "
"Initial treatment depends on presentation: for ketosis or ketoacidosis, insulin is started; once acidosis resolves, metformin is added and insulin is tapered. "
"For HbA1c < 8.5% without acidosis, metformin is the initial agent; GLP-1 RAs (liraglutide, exenatide extended release, dulaglutide) are approved options for age >= 10. "
"The HbA1c target is generally < 7% for most youth, with complication screening (retinopathy, nephropathy, neuropathy, blood pressure, lipids) starting at diagnosis. "
"Lifestyle intervention with at least 60 minutes of daily physical activity is recommended."
)
},

]


def get_all_documents() -> List[Dict[str, Any]]:
    """Return all curated Type 2 Diabetes knowledge documents."""
    return T2DM_KNOWLEDGE_DOCUMENTS


def get_document_by_id(doc_id: str) -> Dict[str, Any]:
    """Retrieve document by ID."""
    for doc in T2DM_KNOWLEDGE_DOCUMENTS:
        if doc["id"] == doc_id:
            return doc
    return {}
