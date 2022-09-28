# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:35:51 2022

@author: manas
"""
import streamlit as st
st.set_page_config(page_title="Understanding Clinical Risk in Value Based Arrangements", page_icon=":tada:")

header_container = st.container()
#side_container= st.sidebar()
defs_container = st.container()
main_container = st.container()
ref_container = st.container()

st.sidebar.header("""Managed Care Activities""")

st.sidebar.write("""
Admin and Network Management
-Claims Administration
-Compliance Management
-Credentialing
-Delegated Oversight Management
-Quality 

Financial Management
-Actuarial Services & Financial Reporting 


Provider Member Services
-Contract Management
-Provider Relations
-Practices Liaison

Care Management & Population Health
-Embedded Care Management
-Remote Care Management
-Specialty Program Optimization
-Behavioral Health
-Clinical Pharmacy
-Care Model and Guidelines
-Quality Program Design
-Utilization Management 
-Member and Provider Services/Call Center

""")


with header_container:
	# for example a logo or a image that looks like a website header
	# different levels of text you can include in your app
    st.title("Understanding Clinical Risk in Value Based Arrangements")
    st.subheader("I welcome comments, feedback and opportunity to learn more or collaborate. Tweet @manas8u")


with main_container:
    st.subheader("What is risk?")
    st.write("""
In this document, I will be focussing on elements of risk relevant to Value Based Care and therefore, risk would mean financial risk with respect to health insurance premiums. Two dimensions are of particular relevance to this discussion of financial risk: (1) objective risk and (2) subjective risk. Objective risk is when the risk inherent in an uncertain outcome is known. For example, the flip of a coin has only objective risk. It is uncertain whether the flip will result in a head or a tail, so the flip is risky, but the probability of flipping a head or tail, 50 percent, is known. Probability of a 65 year old male needing a coronary artery bypass (and its associated costs) are an example of objective risk. Subjective risk occurs when the probability distribution itself is uncertain. For example, a particular weather forecaster may predict that the chance of rain is 20 percent, but different forecasters may attach different probabilities to the event. This occurs with events that are rare with respect to attribution size (e.g. Covid, Transplant related costs). Managing objective risk is a key activity of health insurance organizations and when provider organizations accept risk. This requires provider organizations to develop and use tools such as Utilization Management, Disease Management/Care Management,Risk Management while also maintaining necessary financial reserves to cover the subjective risks assumed by insurance companies.""")

    st.image('https://raw.githubusercontent.com/mangospace/understanding_risk/main/VBC-fig2.webp', caption='Continiuum of premium risk born by providers')
    st.write("""Providers and provider organizations bear financial risk (with respect to insurance premiums) on continiuum. Providers can start at one part of continum and might move to different part of continuum by contracting with different payers. Sometimes providers could be contracting with same payor on different arrangements e.g. organizations might be in a Medicare Shared Savings ACO while also participating in a bundled program.""")

    st.subheader("Why providers consider risk?")
    st.write("""Providers and provider organizations consider risk for diverse reasons. However, the commonly offered reasons are""")
    st.write("""
1. Maintain and/or grow their members, services, fees, and/or revenue
2. Manage or reduce their operating expenses (internal efficiency, consolidation,etc.)
3. Control their time and workload
4. Maintain and/or grow their net income (earnings) – which is their primary financial goal
5. Reduce wasted services across the entire system 
""")
    st.image('https://raw.githubusercontent.com/mangospace/understanding_risk/main/6244ab9551507d05fe2258a7_1_KIQCFFsov3yyTptNdVjkRQ.jpeg', caption='Financial reason why providers consider risk models Source: Caliri (2020)')


    st.write("""Risk arrangements typically fall into one of three categories: primary care capitation, professional services capitation, and global, or full-risk, capitation. Organizations bearing capitation can contractually 'distribute' risk e.g. institutional subcapitation or specialist subcapitation.""")
    st.write("""In global capitation, an payor passes on to a provider organization all or most of the amount of the premium dollar allocated to pay for physician services, including hospital, skilled nursing facility, and home health, and for ancillary services, including laboratory and ambulance, durable medical equipment, and sometimes a part of pharmaceutical costs. Full risk capitation gives a medical group control over approximately 80% of the premium dollar, more leverage in negotiating contracts with hospitals, specialists, and ancillary service
providers, more cash flow to invest in creating utilization management and quality improvement systems, the opportunity to retain all the profit from savings these systems generate, the opportunity to develop wider expertise in managing care, and the opportunity to better coordinate care and to allocate dollars where they will have the most impact on patients’ health. As organizations accept this risk (and premium), payors can delegate/accompany this risk transfer by ensuring that the capitated group provide services to offset/manage risk e.g. Utilization Management and Care Management. In this process, the physician organizations generally use their own standards of care and treatment guidelines, approved by the payors but not dictated by them, to assure consistency and appropriateness in patient treatment. Depending on provider and payor experience and sophistication, payors might retain some elements of managed care services e.g. Credentialing, Claims payment, Network, Appeals, Contracting, Marketing (see sidebar). Depending on the size and stage of maturity, payor might even retain some elements deemed less critical for managing risk e.g. Credentialing or Utilziation of Home Health/DME. In California, only an organization with a special state license (known as a limited Knox-Keene license) is permitted to assume global risk for both professional and institutional services in California. In CMS Direct Contracting Global Model/Total Care Capitation (TCC), the capitated entities are capitated for any eligible Part A and Part B service provided to an attributed beneficiaries with certain exceptions (e.g., claims that contain any substance abuse service or claims from beneficiaries who have opted out of data sharing will not be included).""")

    st.image('https://raw.githubusercontent.com/mangospace/understanding_risk/main/Example%20of%20risk%20contract%20between%20a%20provider%20and%20payor.jpg', caption='Early example of a risk contract')
             
    st.write("""In professional services capitation, a physician organization receives capitation payments only for all services of health care professionals; the payor and contracted physician organization usually have shared risk for institutional services (such as those delivered by a hospital, a nursing home, outpatient surgical facilities, or home health). The payor pays the PMPM amount for professional services to the physician organization directly and sets aside the agreed-upon PMPM amount for institutional services in a risk pool. The payor pays hospitals and other facilities for the services they provide and divides any money left in the pool with the physician organization. If there is a shortfall in pool funds, the physician organization and payor share that liability as well(Foote , 1998).The physician organization could be a multispeciality group or might be a primary care group manages risk through contracting with specialists. Specialty managed care contracting requires all parties to understand their role in managing care, as well as carve-out and subcapitation agreements. The same way, specialists that are contracting or recieving subcapitation need to know their referral sources, their costs for providing care, and how to provide care that meets their referral sources' needs and the payers' requirements, capitated entity needs to understand the 'leakage' out of speciality network as well as service area, cost of specialist services and procedures and as well as opportunitues to manage utilization, improve quality, patient satisfaction (Alexander 1999).""")

    st.write("""In Primary Care Capitation, groups receive capitation for primary care services only as agreed upon based on CPT/HCPCS codes. For example, in CMS Direct Contracting Model Global and Professional Options following class of services are considered for capitation.
-Administration of HRA
-Office or Other Outpatient Services
-Domiciliary, Rest Home, or Custodial Care Services
-Professional Services Provided in a Non-Skilled Nursing Facility
-Domiciliary, Rest Home, or Home Care Plan Oversight Services
-Home Services
-Prolonged Care for Outpatient Visit
-Telephone Visits – Online Digital or Audio Only
-Chronic Care Management (CCM) Services
-Behavioral Health Integration (BHI) Services
-Transitional Care Management Services
-Advance Care Planning
-Wellness Visits
-Depression and Alcohol Misuse

Source:[Direct Contracting Model Global and Professional Options Financial Operating Policies: Capitation and Advanced Payment Mechanisms](https://github.com/mangospace/understanding_risk/blob/536d07979a2382fb150fae1b683275622a12a32a/CapitationAdvPayMechanisms-pages-21-23.pdf)""")

	
    st.subheader("Risk Corridors")
    st.write("""Risk corridors cap the shared savings/losses based on “risk bands” in a capitated agreement meaning that greater deviance from the Performance Year Benchmark will move the capitated entity to the next risk band, resulting in a lower percentage of shared savings/losses for experience within the higher band. For example, a DCE in the Professional Option would experience 50% of savings and losses within 5% of the benchmark, but would be exposed to only 35% of losses more than 5% above the benchmark (up to 10%, where another band with still-lower exposure would begin.""")
    st.image('https://raw.githubusercontent.com/mangospace/understanding_risk/main/risk%20corridors.jpg', caption='Example of risk corridors in CMS Direct Contracting Source: Norris, 2020')
    st.subheader("Stop-loss arrangements")
    st.write("""These prospective arrangements help capitated groups manage risk associated with outlier expenditures by limiting capitated entities financial liability for beneficiary expenditures above a prospectively determined cutoff. Depending on the arrangement between organizations, these arrangements might limit but not eliminate the financial risk by sharing the responsibility of cost such as a percentage of expenditures above the cut off, as incentive to continue managing costs.""")


with ref_container:
    st.subheader("References")
    st.write('Foote SM, Sprague L. Physician Organizations Assuming Risk: Market and Policy Implications Washington (DC): National Health Policy Forum; 1998 Nov 9.https://www.ncbi.nlm.nih.gov/books/NBK560461/')
    st.write('American College of Healthcare Executives Chapter 20: Capitation, Rate Setting, and Risk Sharing https://docplayer.net/59329113-Chapter-20-capitation-rate-setting-and-risk-sharing.html')
    st.write('Casalino L, Robinson J The evolution of medical groups and capitation in California (1997) Kaiser Family Foundation https://www.chcf.org/wp-content/uploads/2017/12/PDF-casalino.pdf')
    st.write('Foote SM, Sprague L Physician Organizations Assuming Risk: Market and Policy Implications Issue Brief, No. 727 Washington (DC): National Health Policy Forum; 1998 Nov 9.')    
    st.write("Vigen GJ,Wernicke MD, Edward M, Pudlowski EM Value-Based Care through Physician Groups An Actuarial Business Perspective (2020) https://www.ccactuaries.org/docs/default-source/papers/physician-based-care-(august-2020).pdf?sfvrsn=bfd42889_5") 
    st.write("Caliri S, Why you should build in primary care: a layman’s guide to risk delegation (2020) https://www.8vc.com/resources/why-you-should-build-in-primary-care-a-laymans-guide-to-risk-delegation")
    st.write("Alexander JM Managed care contracting for specialists Healthc Financ Manage 1999;Suppl:6-10.")
    st.write("Norris C, Jensen B, Grzeskowiak D Direct Contracting: A program summary and comparison with MSSP and NGACO (2020) https://us.milliman.com/-/media/milliman/pdfs/articles/direct_contracting_a_program_summary_and_comparison_with_mssp_and_ngaco.ashx")



    

