# IMPORTING MODULES
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .dbconfig import Base


# CREATING CLASSES FOR SQL TABLE

# Fixed Data
countries_list = Enum('afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi', "côte d'ivoire", 'cabo verde', 'cambodia', 'cameroon', 'canada', 'central african republic', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo (congo-brazzaville)', 'costa rica', 'croatia', 'cuba', 'cyprus', 'czechia (czech republic)', 'democratic republic of the congo', 'denmark', 'djibouti', 'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'eswatini (fmr. "swaziland")', 'ethiopia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 'guinea', 'guinea-bissau', 'guyana', 'haiti', 'holy see', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar (formerly burma)', 'namibia', 'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'north korea', 'north macedonia', 'norway', 'oman', 'pakistan', 'palau', 'palestine state', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda', 'saint kitts and nevis', 'saint lucia', 'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan', 'spain', 'sri lanka', 'sudan', 'suriname', 'sweden', 'switzerland', 'syria', 'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'tonga', 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states of america', 'uruguay', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe', name='country')

categories_list = Enum('accounting', 'administrative', 'advertising', 'agriculture', 'arts_and_design', 'banking', 'biotechnology', 'business_development', 'consulting', 'customer_service', 'education', 'engineering', 'finance', 'healthcare', 'human_resources', 'information_technology', 'legal', 'manufacturing', 'marketing', 'media_and_communications', 'nonprofit', 'retail', 'sales', 'science', 'sports_and_recreation', 'telecommunications', 'transportation_and_logistics', 'travel_and_tourism', 'utilities', name='main categories')

sub_categories_list = Enum('accountants', 'auditors', 'financial_analysts', 'tax_consultants', 'forensic_accountants', 'cost_accountants', 'internal_auditors', 'payroll_clerks', 'bookkeepers', 'compliance_officers', 'investment_accountants', 'management_accountants', 'project_accountants', 'government_accountants', 'environmental_accountants', 'nonprofit_accountants', 'forex_traders', 'real_estate_accountants', 'mergers_and_acquisitions_analysts', 'credit_analysts', 'administrative_assistants', 'office_managers', 'receptionists', 'data_entry_clerks', 'executive_assistants', 'office_coordinators', 'office_administrators', 'file_clerks', 'records_managers', 'mailroom_clerks', 'facilities_managers', 'document_control_specialists', 'front_desk_coordinators', 'calendar_managers', 'office_supervisors', 'office_planners', 'inventory_control_clerks', 'clerical_support_specialists', 'conference_coordinators', 'billing_coordinators', 'advertising_executives', 'copywriters', 'media_planners', 'marketing_specialists', 'art_directors', 'digital_marketers', 'brand_strategists', 'social_media_managers', 'content_creators', 'media_buyers', 'ad_operations_managers', 'seo_specialists', 'advertising_designers', 'market_researchers', 'public_relations_specialists', 'campaign_managers', 'advertising_sales_representatives', 'account_coordinators', 'creative_directors', 'media_analysts', 'traffic_managers', 'agricultural_scientists', 'farmers', 'agribusiness_professionals', 'horticulturists', 'livestock_managers', 'agricultural_engineers', 'crop_consultants', 'soil_scientists', 'animal_nutritionists', 'pest_control_specialists', 'agricultural_economists', 'aquaculturists', 'dairy_farmers', 'sustainable_agriculture_specialists', 'irrigation_technicians', 'seed_breeders', 'precision_agriculture_technologists', 'agricultural_extension_officers', 'viticulturists', 'food_safety_inspectors', 'graphic_designers', 'artists', 'illustrators', 'photographers', 'fashion_designers', 'web_designers', 'interior_designers', 'industrial_designers', 'ui/ux_designers', 'multimedia_artists', 'animation_designers', 'video_game_designers', 'museum_curators', 'gallery_managers', 'art_conservators', 'art_teachers', 'set_designers', 'creative_directors', 'storyboard_artists', 'fine_arts_painters', 'tattoo_artists', 'bankers', 'financial_analysts', 'loan_officers', 'investment_professionals', 'risk_analysts', 'mortgage_specialists', 'credit_analysts', 'branch_managers', 'tellers', 'wealth_managers', 'compliance_officers', 'private_bankers', 'commercial_bankers', 'treasury_analysts', 'quantitative_analysts', 'fixed_income_traders', 'investment_banking_associates', 'retail_bankers', 'asset_managers', 'derivatives_traders', 'biologists', 'biochemists', 'research_scientists', 'biotech_engineers', 'pharmacologists', 'geneticists', 'microbiologists', 'clinical_research_coordinators', 'lab_technicians', 'bioprocess_engineers', 'regulatory_affairs_specialists', 'quality_control_analysts', 'bioinformatics_analysts', 'molecular_biologists', 'cell_biologists', 'proteomics_scientists', 'stem_cell_researchers', 'immunologists', 'biotech_sales_representatives', 'biomanufacturing_specialists', 'bioethicists', 'business_development_managers', 'sales_representatives', 'partnerships_specialists', 'market_research_analysts', 'sales_strategists', 'lead_generation_specialists', 'client_relationship_managers', 'channel_sales_managers', 'sales_trainers', 'sales_operations_analysts', 'growth_hackers', 'sales_coordinators', 'sales_enablement_managers', 'strategic_account_managers', 'sales_engineers', 'franchise_development_managers', 'proposal_writers', 'customer_retention_specialists', 'market_expansion_strategists', 'innovation_consultants', 'management_consultants', 'strategy_consultants', 'business_advisors', 'financial_consultants', 'it_consultants', 'hr_consultants', 'marketing_consultants', 'change_management_consultants', 'organizational_development_specialists', 'process_improvement_consultants', 'supply_chain_consultants', 'legal_consultants', 'environmental_consultants', 'healthcare_consultants', 'government_policy_consultants', 'data_analytics_consultants', 'nonprofit_consultants', 'retail_consultants', 'economic_consultants', 'education_consultants', 'customer_support_representatives', 'call_center_agents', 'client_success_managers', 'technical_support_specialists', 'complaint_resolution_specialists', 'customer_service_supervisors', 'quality_assurance_analysts', 'chat_support_agents', 'email_support_specialists', 'escalation_specialists', 'customer_service_trainers', 'social_media_customer_service_agents', 'billing_and_payments_specialists', 'vip_customer_service_representatives', 'order_fulfillment_specialists', 'customer_experience_designers', 'customer_satisfaction_analysts', 'multilingual_customer_service_agents', 'emergency_support_specialists', 'field_service_technicians', 'teachers', 'professors', 'educational_consultants', 'school_administrators', 'tutors', 'school_counselors', 'curriculum_developers', 'special_education_teachers', 'esl_instructors', 'online_educators', 'instructional_designers', 'adult_education_instructors', 'education_policy_analysts', 'career_counselors', 'education_researchers', 'early_childhood_educators', 'school_librarians', 'principal_administrators', 'education_technology_specialists', 'montessori_teachers', 'civil_engineers', 'mechanical_engineers', 'electrical_engineers', 'software_engineers', 'chemical_engineers', 'aerospace_engineers', 'environmental_engineers', 'biomedical_engineers', 'structural_engineers', 'industrial_engineers', 'automotive_engineers', 'petroleum_engineers', 'materials_engineers', 'systems_engineers', 'robotics_engineers', 'mining_engineers', 'nuclear_engineers', 'marine_engineers', 'water_resources_engineers', 'acoustic_engineers', 'finance_managers', 'financial_planners', 'investment_bankers', 'financial_analysts', 'hedge_fund_managers', 'risk_analysts', 'credit_analysts', 'venture_capitalists', 'private_equity_analysts', 'wealth_managers', 'compliance_officers', 'quantitative_analysts', 'derivatives_traders', 'portfolio_managers', 'fixed_income_analysts', 'corporate_treasurers', 'financial_controllers', 'real_estate_analysts', 'tax_consultants', 'mergers_and_acquisitions_advisors', 'doctors', 'nurses', 'pharmacists', 'healthcare_administrators', 'medical_researchers', 'physical_therapists', 'occupational_therapists', 'dentists', 'surgeons', 'radiologists', 'psychiatrists', 'nutritionists', 'clinical_lab_technicians', 'emergency_medical_technicians', 'health_informatics_specialists', 'medical_imaging_technologists', 'medical_social_workers', 'hospital_administrators', 'nurse_practitioners', 'medical_transcriptionists', 'hr_managers', 'recruiters', 'benefits_specialists', 'training_coordinators', 'compensation_analysts', 'talent_acquisition_specialists', 'employee_relations_managers', 'hr_generalists', 'hr_consultants', 'labor_relations_specialists', 'hr_information_systems_managers', 'diversity_and_inclusion_managers', 'hr_business_partners', 'hr_directors', 'employment_law_specialists', 'workforce_planners', 'health_and_safety_specialists', 'hr_analytics_experts', 'onboarding_specialists', 'change_management_consultants', 'software_developers', 'it_managers', 'cybersecurity_specialists', 'data_analysts', 'network_administrators', 'web_developers', 'database_administrators', 'system_architects', 'cloud_engineers', 'devops_engineers', 'ui/ux_designers', 'qa_testers', 'artificial_intelligence_engineers', 'machine_learning_engineers', 'network_security_analysts', 'mobile_app_developers', 'front-end_developers', 'back-end_developers', 'it_support_technicians', 'enterprise_architects', 'lawyers', 'paralegals', 'legal_assistants', 'legal_consultants', 'legal_secretaries', 'legal_researchers', 'corporate_counsel', 'criminal_defense_attorneys', 'immigration_lawyers', 'intellectual_property_lawyers', 'family_law_attorneys', 'bankruptcy_attorneys', 'environmental_lawyers', 'contract_lawyers', 'tax_attorneys', 'estate_planning_attorneys', 'litigation_attorneys', 'employment_lawyers', 'real_estate_attorneys', 'international_trade_lawyers', 'factory_workers', 'production_managers', 'quality_control_specialists', 'supply_chain_professionals', 'plant_managers', 'manufacturing_engineers', 'industrial_designers', 'process_engineers', 'operations_supervisors', 'maintenance_technicians', 'safety_managers', 'logistics_coordinators', 'lean_manufacturing_specialists', 'inventory_managers', 'materials_planners', 'automation_engineers', 'six_sigma_black_belts', 'continuous_improvement_specialists', 'packaging_engineers', 'machine_operators', 'marketers', 'marketing_managers', 'seo_specialists', 'content_creators', 'brand_managers', 'product_managers', 'digital_marketing_specialists', 'market_research_analysts', 'public_relations_specialists', 'social_media_managers', 'email_marketing_specialists', 'event_planners', 'advertising_coordinators', 'marketing_analytics_experts', 'influencer_marketers', 'direct_marketing_specialists', 'marketing_automation_specialists', 'copy_editors', 'media_buyers', 'market_segmentation_analysts', 'consumer_behavior_analysts', 'journalists', 'pr_professionals', 'social_media_managers', 'communication_specialists', 'broadcasters', 'writers', 'editors', 'content_producers', 'photojournalists', 'media_relations_specialists', 'news_anchors', 'radio_hosts', 'advertising_copywriters', 'press_release_writers', 'multimedia_journalists', 'crisis_communications_specialists', 'film_directors', 'tv_producers', 'public_affairs_specialists', 'documentary_filmmakers', 'charity_workers', 'nonprofit_executives', 'grant_writers', 'program_managers', 'fundraisers', 'community_outreach_coordinators', 'volunteer_coordinators', 'advocacy_specialists', 'nonprofit_consultants', 'social_workers', 'humanitarian_aid_workers', 'environmental_activists', 'youth_counselors', 'international_development_specialists', 'nonprofit_marketing_managers', 'public_policy_analysts', 'event_planners', 'nonprofit_accountants', 'foundation_directors', 'nonprofit_lawyers', 'store_managers', 'sales_associates', 'merchandisers', 'e-commerce_specialists', 'visual_merchandisers', 'retail_buyers', 'loss_prevention_specialists', 'inventory_managers', 'retail_marketers', 'customer_service_representatives', 'fashion_stylists', 'retail_planners', 'category_managers', 'stock_clerks', 'retail_analysts', 'store_designers', 'retail_operations_managers', 'vendor_relations_specialists', 'franchise_owners', 'fashion_designers', 'retail_trainers', 'sales_representatives', 'account_executives', 'business_development_specialists', 'sales_managers', 'sales_coordinators', 'inside_sales_representatives', 'outside_sales_representatives', 'sales_trainers', 'technical_sales_specialists', 'channel_sales_managers', 'key_account_managers', 'sales_engineers', 'customer_success_managers', 'sales_operations_managers', 'sales_enablement_specialists', 'sales_support_specialists', 'sales_forecast_analysts', 'regional_sales_directors', 'enterprise_sales_executives', 'sales_development_representatives', 'retail_sales_associates', 'chemists', 'physicists', 'environmental_scientists', 'biologists', 'astronomers', 'geologists', 'oceanographers', 'ecologists', 'zoologists', 'materials_scientists', 'nanotechnologists', 'forensic_scientists', 'neuroscientists', 'astrophysicists', 'microbiologists', 'seismologists', 'quantum_physicists', 'botanists', 'entomologists', 'epidemiologists', 'athletes', 'coaches', 'sports_analysts', 'sports_management_professionals', 'physical_therapists', 'nutritionists', 'sports_psychologists', 'sports_medicine_physicians', 'strength_and_conditioning_coaches', 'scouts', 'athletic_trainers', 'referees', 'event_managers', 'sports_marketers', 'sports_journalists', 'sports_photographers', 'sports_agents', 'groundskeepers', 'sports_broadcasters', 'sports_engineers', 'sports_statisticians', 'telecom_engineers', 'network_administrators', 'telecom_sales_professionals', 'telecom_technicians', 'wireless_communication_specialists', 'telecom_project_managers', 'voip_engineers', 'network_security_analysts', 'fiber_optic_technicians', 'telecom_consultants', 'telecom_regulatory_specialists', 'rf_engineers', 'satellite_communication_specialists', 'telecom_software_developers', 'telecom_systems_architects', 'switchboard_operators', 'telecom_maintenance_technicians', 'telecom_account_managers', 'telecom_customer_support_specialists', 'telecom_billing_analysts', 'network_design_engineers', 'truck_drivers', 'logistics_coordinators', 'supply_chain_managers', 'transportation_planners', 'fleet_managers', 'warehouse_supervisors', 'route_planners', 'freight_brokers', 'shipping_clerks', 'customs_brokers', 'dispatcher_operators', 'import/export_specialists', 'logistics_analysts', 'pilots', 'air_traffic_controllers', 'marine_navigators', 'port_operators', 'railroad_conductors', 'transit_drivers', 'material_handlers', 'courier_and_delivery_drivers', 'travel_agents', 'tour_guides', 'hospitality_professionals', 'airline_employees', 'cruise_directors', 'hotel_managers', 'reservations_agents', 'travel_consultants', 'event_planners', 'adventure_tour_leaders', 'cultural_heritage_guides', 'destination_marketers', 'meeting_and_convention_planners', 'sustainable_tourism_specialists', 'customer_experience_managers', 'tourism_researchers', 'food_and_beverage_managers', 'travel_writers', 'travel_photographers', 'airport_staff', 'energy_sector_professionals', 'electricians', 'power_plant_operators', 'renewable_energy_specialists', 'utility_technicians', 'grid_operators', 'water_treatment_operators', 'gas_technicians', 'energy_efficiency_consultants', 'pipeline_operators', 'meter_readers', 'wastewater_treatment_technicians', 'electrical_engineers', 'environmental_compliance_specialists', 'utility_inspectors', 'field_service_technicians', 'telecom_power_technicians', 'nuclear_plant_operators', 'hydropower_technicians', 'solar_panel_installers', name='sub category')


# LOCATION TABLE
class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    # data_id = Column(String(30), unique=True, nullable=False)
    country = Column(countries_list)
    state = Column(String(20), nullable=True)
    division = Column(String(30), nullable=True)
    city = Column(String(30), nullable=True)
    address = Column(String(100), nullable=True)
    zip_code = Column(String(20), nullable=True)
    # map_url = Column(String(500), nullable=True)

    loc_user = relationship('User', back_populates='sec_loc')
    loc_company = relationship('Company', back_populates='sec_loc')
    loc_job = relationship('Job', back_populates='sec_loc')


# SOCIAL MEDIA TABLE
class Social(Base):
    __tablename__ = 'socials'

    id = Column(Integer, primary_key=True, index=True)
    # data_id = Column(String(30), unique=True, nullable=False)
    facebook = Column(String(100), nullable=True)
    linkedin = Column(String(100), nullable=True)
    twitter = Column(String(100), nullable=True)
    instagram = Column(String(100), nullable=True)
    whatsapp = Column(String(100), nullable=True)

    soc_company = relationship('Company', back_populates='sec_social')


# USERS TABLE
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20), nullable=True)
    last_name = Column(String(20), nullable=True)
    birth_date = Column(DateTime, nullable=False)
    email = Column(String(30), unique=True, index=True, nullable=False)
    location = Column(String(30), ForeignKey('locations.id', ondelete='SET NULL'), nullable=True)
    username = Column(String(30), unique=True, index=True, nullable=False)
    is_refugee = Column(Boolean, default=False, nullable=False)

    sec_loc = relationship('Location', back_populates='loc_user')
    apply_to = relationship('Application', back_populates='applicant')


# COMPANY TABLE
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    c_name = Column(String(30), unique=True, nullable=False, index=True)
    c_mail = Column(String(30), unique=True, nullable=False, index=True)
    social = Column(String(30), ForeignKey('socials.id', ondelete='SET NULL'), nullable=True)
    location = Column(String(30), ForeignKey('locations.id', ondelete='SET NULL'), nullable=True)
    website = Column(String(100), nullable=True)

    job = relationship('Job', back_populates='owner')
    sec_loc = relationship('Location', back_populates='loc_company')
    sec_social = relationship('Social', back_populates='soc_company')


# JOB TABLE
class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    # name_id = Column(String(50), unique=True, nullable=False)
    job_title = Column(String(500), nullable=False)
    company = Column(String(30), ForeignKey('companies.c_name'))
    job_type = Column(Enum("fixed_price", "full_time", "part_time", "freelance", name="job type"))
    posted_on = Column(DateTime, server_default=func.now())
    location = Column(String(30), ForeignKey('locations.data_id'))
    salary_amount = Column(Float(precision=2))
    salary_duration = Column(Enum("weekly", "monthly", "hourly", name="salary type"))
    category = Column(Enum(categories_list))
    sub_category = Column(sub_categories_list)
    overview = Column(String(1500), nullable=True)
    job_description = Column(String(3000))
    experience = Column(Enum("fresher", "no_experience", "expert", "internship", "intermediate", name="experience level"))
    responsibility = Column(String(2000), nullable=True)
    required_skills = Column(String(500), nullable=True)
    benefits = Column(String(1500), nullable=True)
    job_url = Column(String(100), nullable=True)

    owner = relationship('Company', back_populates='job')
    sec_loc = relationship('Location', back_populates='loc_job')
    application = relationship('Application', back_populates='')
    


# ACCOUNT TABLE
class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    login_name = Column(String(30), unique=True, nullable=False, index=True)
    login_email = Column(String(30), unique=True, nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    role = Column(Enum("user", "company", "developer", "admin", name="account role"), nullable=False)


# JOB APPLY TABLE
class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    user_acc = Column(String(30), ForeignKey('users.username'))
    job_id = Column(String(50), ForeignKey('jobs.id'))
    applied_on = Column(DateTime, server_default=func.now())
    cover_letter = Column(String(2000), nullable=True)

    applicant = relationship('User', back_populates='apply_to')
    applied_job = relationship('Job', back_populates='application')


# APPLICATION LETTER
