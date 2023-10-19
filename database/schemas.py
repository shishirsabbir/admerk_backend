# IMPORTING MODULES
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


# CREATING PYDANTIC CLASSES FOR LOCATION MODEL
class LocationModel(BaseModel):
    # data_id: str
    country: Literal['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi', "côte d'ivoire", 'cabo verde', 'cambodia', 'cameroon', 'canada', 'central african republic', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo (congo-brazzaville)', 'costa rica', 'croatia', 'cuba', 'cyprus', 'czechia (czech republic)', 'democratic republic of the congo', 'denmark', 'djibouti', 'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'eswatini (fmr. "swaziland")', 'ethiopia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 'guinea', 'guinea-bissau', 'guyana', 'haiti', 'holy see', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar (formerly burma)', 'namibia', 'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'north korea', 'north macedonia', 'norway', 'oman', 'pakistan', 'palau', 'palestine state', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda', 'saint kitts and nevis', 'saint lucia', 'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan', 'spain', 'sri lanka', 'sudan', 'suriname', 'sweden', 'switzerland', 'syria', 'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'tonga', 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states of america', 'uruguay', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe']
    state: str | None = Field(max_length=30)
    division: str | None = Field(max_length=30)
    city: str | None = Field(max_length=30)
    address: str | None = Field(max_length=100)
    zip_code: str | None = Field(max_length=20)



# CREATING PYDANTIC CLASSES FOR SOCIAL MODEL
class SocialModel(BaseModel):
    # data_id: str
    facebook: str | None = Field(max_length=100)
    linkedin: str | None = Field(max_length=100)
    twitter: str | None = Field(max_length=100)
    instagram: str | None = Field(max_length=100)
    whatsapp: str | None = Field(max_length=100)



# CREATING PYDANTIC CLASSES FOR USER'S ACCOUNT MODEL
class UserModel(BaseModel):
    first_name: str | None = Field(max_length=30, default=None)
    last_name: str | None = Field(max_length=30, default=None)
    birth_date: datetime = Field(default=datetime(year=1996, month=5, day=8))
    email: str = Field(max_length=30)
    location: LocationModel | None = None
    username: str = Field(max_length=30)
    password: str = Field(min_length=8)
    is_refugee: bool = Field(default=False)
    role: str = Field(default="user")

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "arno",
                    "last_name": "liono",
                    "birth_date": "1999-05-08T00:00:00",
                    "email": "arnoliono@gmail.com",
                    "location": {
                        "country": "bangladesh",
                        "state": "",
                        "division": "rajshahi",
                        "city": "rajshahi"
                    },
                    "username": "arnoliono",
                    "password": "@Test1234",
                    "is_refugee": False
                }
            ]
        }
    }


# CREATE PYDANTIC CLASS FOR COMPANY'S ACCOUNT MODEL
class CompanyModel(BaseModel):
    name: str = Field(max_length=30)
    c_name: str = Field(max_length=30)
    c_mail: str = Field(max_length=30)
    password: str = Field(min_length=8)
    social: SocialModel | None = None
    location: LocationModel | None = None
    website: str = Field(max_length=100)
    role: str = Field(default='company')

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "pepsico",
                    "c_name": "pepsicouk",
                    "c_mail": "company@pepsico.co.uk",
                    "password": "@Test1234",
                    "social": {
                        "facebook": "https://www.facebook.com/pepsicouk",
                        "linkedin": "https://www.pepsicouk.com/pepsicouk",
                        "twitter": "https://www.twitter.com/pepsicouk",
                        "instagram": "https://www.instagram.com/pepsicouk",
                        "whatsapp": "https://wa.me/message/2UQHWE2LXVUDF1/pepsicouk"
                    },
                    "location": {
                        "country": "united kingdom",
                        "state": "greater manchester",
                        "division": "",
                        "city": "manchester"
                    },
                    "website": "https://www.pepsicouk.com"
                }
            ]
        }
    }


# PYDANTIC CLASSES FOR JWT TOKEN, CREATE ACCOUNT, PASSWORD CHANGE REQUEST
class Token(BaseModel):
    access_token: str
    token_type: str
    login_data: dict | None = None


# PYDANTIC CLASSES PASSWORD CHANGE REQUEST
class ChangePasswordRequest(BaseModel):
    password: str = Field(min_length=8)
    new_password: str = Field(min_length=8)

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "password": "@Test1234",
                    "new_password": "@Test12345"
                }
            ]
        }
    }


# PYDANTIC CLASS FOR LOGIN ACCOUNT MODEL
class AccountModel(BaseModel):
    login_name: str = Field(max_length=30)
    login_email: str = Field(max_length=30)
    hashed_password: str = Field(min_length=8)
    role: Literal["user", "company", "developer", "admin"]


# PYDANTIC CLASS FOR CREATE ACCOUNT MODEL
class AccountModelCreate(BaseModel):
    login_name: str = Field(max_length=30)
    login_email: str = Field(max_length=30)
    password: str
    role: Literal["user", "company", "developer", "admin"]

    model_config= {
            "json_schema_extra": {
                "examples": [
                    {
                        "login_name": "shishirsabbir",
                        "login_email": "shishir.sabbir@gmail.com",
                        "password": "@Test1234",
                        "role": "admin"
                    }
                ]
            }
        }



class ValidateRequest(BaseModel):
    username: str | None = None
    email: str | None = None

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "username/email": "username/user@mail.com"
                }
            ]
        }
    }


# PYDANTIC CLASS FOR JOB MODEL
class JobModel(BaseModel):
    # name_id: str = Field(max_length=50)
    job_title: str = Field(max_length=500)
    # company: str = Field(max_length=30)
    job_type: Literal["fixed_price", "full_time", "part_time", "freelance"]
    # posted_on: datetime
    location: LocationModel | None = None
    salary_amount: float | None = None
    salary_duration: Literal["weekly", "monthly", "hourly"]
    category: Literal['accounting', 'administrative', 'advertising', 'agriculture', 'arts_and_design', 'banking', 'biotechnology', 'business_development', 'consulting', 'customer_service', 'education', 'engineering', 'finance', 'healthcare', 'human_resources', 'information_technology', 'legal', 'manufacturing', 'marketing', 'media_and_communications', 'nonprofit', 'retail', 'sales', 'science', 'sports_and_recreation', 'telecommunications', 'transportation_and_logistics', 'travel_and_tourism', 'utilities']
    sub_category: Literal['accountants', 'auditors', 'financial_analysts', 'tax_consultants', 'forensic_accountants', 'cost_accountants', 'internal_auditors', 'payroll_clerks', 'bookkeepers', 'compliance_officers', 'investment_accountants', 'management_accountants', 'project_accountants', 'government_accountants', 'environmental_accountants', 'nonprofit_accountants', 'forex_traders', 'real_estate_accountants', 'mergers_and_acquisitions_analysts', 'credit_analysts', 'administrative_assistants', 'office_managers', 'receptionists', 'data_entry_clerks', 'executive_assistants', 'office_coordinators', 'office_administrators', 'file_clerks', 'records_managers', 'mailroom_clerks', 'facilities_managers', 'document_control_specialists', 'front_desk_coordinators', 'calendar_managers', 'office_supervisors', 'office_planners', 'inventory_control_clerks', 'clerical_support_specialists', 'conference_coordinators', 'billing_coordinators', 'advertising_executives', 'copywriters', 'media_planners', 'marketing_specialists', 'art_directors', 'digital_marketers', 'brand_strategists', 'social_media_managers', 'content_creators', 'media_buyers', 'ad_operations_managers', 'seo_specialists', 'advertising_designers', 'market_researchers', 'public_relations_specialists', 'campaign_managers', 'advertising_sales_representatives', 'account_coordinators', 'creative_directors', 'media_analysts', 'traffic_managers', 'agricultural_scientists', 'farmers', 'agribusiness_professionals', 'horticulturists', 'livestock_managers', 'agricultural_engineers', 'crop_consultants', 'soil_scientists', 'animal_nutritionists', 'pest_control_specialists', 'agricultural_economists', 'aquaculturists', 'dairy_farmers', 'sustainable_agriculture_specialists', 'irrigation_technicians', 'seed_breeders', 'precision_agriculture_technologists', 'agricultural_extension_officers', 'viticulturists', 'food_safety_inspectors', 'graphic_designers', 'artists', 'illustrators', 'photographers', 'fashion_designers', 'web_designers', 'interior_designers', 'industrial_designers', 'ui/ux_designers', 'multimedia_artists', 'animation_designers', 'video_game_designers', 'museum_curators', 'gallery_managers', 'art_conservators', 'art_teachers', 'set_designers', 'creative_directors', 'storyboard_artists', 'fine_arts_painters', 'tattoo_artists', 'bankers', 'financial_analysts', 'loan_officers', 'investment_professionals', 'risk_analysts', 'mortgage_specialists', 'credit_analysts', 'branch_managers', 'tellers', 'wealth_managers', 'compliance_officers', 'private_bankers', 'commercial_bankers', 'treasury_analysts', 'quantitative_analysts', 'fixed_income_traders', 'investment_banking_associates', 'retail_bankers', 'asset_managers', 'derivatives_traders', 'biologists', 'biochemists', 'research_scientists', 'biotech_engineers', 'pharmacologists', 'geneticists', 'microbiologists', 'clinical_research_coordinators', 'lab_technicians', 'bioprocess_engineers', 'regulatory_affairs_specialists', 'quality_control_analysts', 'bioinformatics_analysts', 'molecular_biologists', 'cell_biologists', 'proteomics_scientists', 'stem_cell_researchers', 'immunologists', 'biotech_sales_representatives', 'biomanufacturing_specialists', 'bioethicists', 'business_development_managers', 'sales_representatives', 'partnerships_specialists', 'market_research_analysts', 'sales_strategists', 'lead_generation_specialists', 'client_relationship_managers', 'channel_sales_managers', 'sales_trainers', 'sales_operations_analysts', 'growth_hackers', 'sales_coordinators', 'sales_enablement_managers', 'strategic_account_managers', 'sales_engineers', 'franchise_development_managers', 'proposal_writers', 'customer_retention_specialists', 'market_expansion_strategists', 'innovation_consultants', 'management_consultants', 'strategy_consultants', 'business_advisors', 'financial_consultants', 'it_consultants', 'hr_consultants', 'marketing_consultants', 'change_management_consultants', 'organizational_development_specialists', 'process_improvement_consultants', 'supply_chain_consultants', 'legal_consultants', 'environmental_consultants', 'healthcare_consultants', 'government_policy_consultants', 'data_analytics_consultants', 'nonprofit_consultants', 'retail_consultants', 'economic_consultants', 'education_consultants', 'customer_support_representatives', 'call_center_agents', 'client_success_managers', 'technical_support_specialists', 'complaint_resolution_specialists', 'customer_service_supervisors', 'quality_assurance_analysts', 'chat_support_agents', 'email_support_specialists', 'escalation_specialists', 'customer_service_trainers', 'social_media_customer_service_agents', 'billing_and_payments_specialists', 'vip_customer_service_representatives', 'order_fulfillment_specialists', 'customer_experience_designers', 'customer_satisfaction_analysts', 'multilingual_customer_service_agents', 'emergency_support_specialists', 'field_service_technicians', 'teachers', 'professors', 'educational_consultants', 'school_administrators', 'tutors', 'school_counselors', 'curriculum_developers', 'special_education_teachers', 'esl_instructors', 'online_educators', 'instructional_designers', 'adult_education_instructors', 'education_policy_analysts', 'career_counselors', 'education_researchers', 'early_childhood_educators', 'school_librarians', 'principal_administrators', 'education_technology_specialists', 'montessori_teachers', 'civil_engineers', 'mechanical_engineers', 'electrical_engineers', 'software_engineers', 'chemical_engineers', 'aerospace_engineers', 'environmental_engineers', 'biomedical_engineers', 'structural_engineers', 'industrial_engineers', 'automotive_engineers', 'petroleum_engineers', 'materials_engineers', 'systems_engineers', 'robotics_engineers', 'mining_engineers', 'nuclear_engineers', 'marine_engineers', 'water_resources_engineers', 'acoustic_engineers', 'finance_managers', 'financial_planners', 'investment_bankers', 'financial_analysts', 'hedge_fund_managers', 'risk_analysts', 'credit_analysts', 'venture_capitalists', 'private_equity_analysts', 'wealth_managers', 'compliance_officers', 'quantitative_analysts', 'derivatives_traders', 'portfolio_managers', 'fixed_income_analysts', 'corporate_treasurers', 'financial_controllers', 'real_estate_analysts', 'tax_consultants', 'mergers_and_acquisitions_advisors', 'doctors', 'nurses', 'pharmacists', 'healthcare_administrators', 'medical_researchers', 'physical_therapists', 'occupational_therapists', 'dentists', 'surgeons', 'radiologists', 'psychiatrists', 'nutritionists', 'clinical_lab_technicians', 'emergency_medical_technicians', 'health_informatics_specialists', 'medical_imaging_technologists', 'medical_social_workers', 'hospital_administrators', 'nurse_practitioners', 'medical_transcriptionists', 'hr_managers', 'recruiters', 'benefits_specialists', 'training_coordinators', 'compensation_analysts', 'talent_acquisition_specialists', 'employee_relations_managers', 'hr_generalists', 'hr_consultants', 'labor_relations_specialists', 'hr_information_systems_managers', 'diversity_and_inclusion_managers', 'hr_business_partners', 'hr_directors', 'employment_law_specialists', 'workforce_planners', 'health_and_safety_specialists', 'hr_analytics_experts', 'onboarding_specialists', 'change_management_consultants', 'software_developers', 'it_managers', 'cybersecurity_specialists', 'data_analysts', 'network_administrators', 'web_developers', 'database_administrators', 'system_architects', 'cloud_engineers', 'devops_engineers', 'ui/ux_designers', 'qa_testers', 'artificial_intelligence_engineers', 'machine_learning_engineers', 'network_security_analysts', 'mobile_app_developers', 'front-end_developers', 'back-end_developers', 'it_support_technicians', 'enterprise_architects', 'lawyers', 'paralegals', 'legal_assistants', 'legal_consultants', 'legal_secretaries', 'legal_researchers', 'corporate_counsel', 'criminal_defense_attorneys', 'immigration_lawyers', 'intellectual_property_lawyers', 'family_law_attorneys', 'bankruptcy_attorneys', 'environmental_lawyers', 'contract_lawyers', 'tax_attorneys', 'estate_planning_attorneys', 'litigation_attorneys', 'employment_lawyers', 'real_estate_attorneys', 'international_trade_lawyers', 'factory_workers', 'production_managers', 'quality_control_specialists', 'supply_chain_professionals', 'plant_managers', 'manufacturing_engineers', 'industrial_designers', 'process_engineers', 'operations_supervisors', 'maintenance_technicians', 'safety_managers', 'logistics_coordinators', 'lean_manufacturing_specialists', 'inventory_managers', 'materials_planners', 'automation_engineers', 'six_sigma_black_belts', 'continuous_improvement_specialists', 'packaging_engineers', 'machine_operators', 'marketers', 'marketing_managers', 'seo_specialists', 'content_creators', 'brand_managers', 'product_managers', 'digital_marketing_specialists', 'market_research_analysts', 'public_relations_specialists', 'social_media_managers', 'email_marketing_specialists', 'event_planners', 'advertising_coordinators', 'marketing_analytics_experts', 'influencer_marketers', 'direct_marketing_specialists', 'marketing_automation_specialists', 'copy_editors', 'media_buyers', 'market_segmentation_analysts', 'consumer_behavior_analysts', 'journalists', 'pr_professionals', 'social_media_managers', 'communication_specialists', 'broadcasters', 'writers', 'editors', 'content_producers', 'photojournalists', 'media_relations_specialists', 'news_anchors', 'radio_hosts', 'advertising_copywriters', 'press_release_writers', 'multimedia_journalists', 'crisis_communications_specialists', 'film_directors', 'tv_producers', 'public_affairs_specialists', 'documentary_filmmakers', 'charity_workers', 'nonprofit_executives', 'grant_writers', 'program_managers', 'fundraisers', 'community_outreach_coordinators', 'volunteer_coordinators', 'advocacy_specialists', 'nonprofit_consultants', 'social_workers', 'humanitarian_aid_workers', 'environmental_activists', 'youth_counselors', 'international_development_specialists', 'nonprofit_marketing_managers', 'public_policy_analysts', 'event_planners', 'nonprofit_accountants', 'foundation_directors', 'nonprofit_lawyers', 'store_managers', 'sales_associates', 'merchandisers', 'e-commerce_specialists', 'visual_merchandisers', 'retail_buyers', 'loss_prevention_specialists', 'inventory_managers', 'retail_marketers', 'customer_service_representatives', 'fashion_stylists', 'retail_planners', 'category_managers', 'stock_clerks', 'retail_analysts', 'store_designers', 'retail_operations_managers', 'vendor_relations_specialists', 'franchise_owners', 'fashion_designers', 'retail_trainers', 'sales_representatives', 'account_executives', 'business_development_specialists', 'sales_managers', 'sales_coordinators', 'inside_sales_representatives', 'outside_sales_representatives', 'sales_trainers', 'technical_sales_specialists', 'channel_sales_managers', 'key_account_managers', 'sales_engineers', 'customer_success_managers', 'sales_operations_managers', 'sales_enablement_specialists', 'sales_support_specialists', 'sales_forecast_analysts', 'regional_sales_directors', 'enterprise_sales_executives', 'sales_development_representatives', 'retail_sales_associates', 'chemists', 'physicists', 'environmental_scientists', 'biologists', 'astronomers', 'geologists', 'oceanographers', 'ecologists', 'zoologists', 'materials_scientists', 'nanotechnologists', 'forensic_scientists', 'neuroscientists', 'astrophysicists', 'microbiologists', 'seismologists', 'quantum_physicists', 'botanists', 'entomologists', 'epidemiologists', 'athletes', 'coaches', 'sports_analysts', 'sports_management_professionals', 'physical_therapists', 'nutritionists', 'sports_psychologists', 'sports_medicine_physicians', 'strength_and_conditioning_coaches', 'scouts', 'athletic_trainers', 'referees', 'event_managers', 'sports_marketers', 'sports_journalists', 'sports_photographers', 'sports_agents', 'groundskeepers', 'sports_broadcasters', 'sports_engineers', 'sports_statisticians', 'telecom_engineers', 'network_administrators', 'telecom_sales_professionals', 'telecom_technicians', 'wireless_communication_specialists', 'telecom_project_managers', 'voip_engineers', 'network_security_analysts', 'fiber_optic_technicians', 'telecom_consultants', 'telecom_regulatory_specialists', 'rf_engineers', 'satellite_communication_specialists', 'telecom_software_developers', 'telecom_systems_architects', 'switchboard_operators', 'telecom_maintenance_technicians', 'telecom_account_managers', 'telecom_customer_support_specialists', 'telecom_billing_analysts', 'network_design_engineers', 'truck_drivers', 'logistics_coordinators', 'supply_chain_managers', 'transportation_planners', 'fleet_managers', 'warehouse_supervisors', 'route_planners', 'freight_brokers', 'shipping_clerks', 'customs_brokers', 'dispatcher_operators', 'import/export_specialists', 'logistics_analysts', 'pilots', 'air_traffic_controllers', 'marine_navigators', 'port_operators', 'railroad_conductors', 'transit_drivers', 'material_handlers', 'courier_and_delivery_drivers', 'travel_agents', 'tour_guides', 'hospitality_professionals', 'airline_employees', 'cruise_directors', 'hotel_managers', 'reservations_agents', 'travel_consultants', 'event_planners', 'adventure_tour_leaders', 'cultural_heritage_guides', 'destination_marketers', 'meeting_and_convention_planners', 'sustainable_tourism_specialists', 'customer_experience_managers', 'tourism_researchers', 'food_and_beverage_managers', 'travel_writers', 'travel_photographers', 'airport_staff', 'energy_sector_professionals', 'electricians', 'power_plant_operators', 'renewable_energy_specialists', 'utility_technicians', 'grid_operators', 'water_treatment_operators', 'gas_technicians', 'energy_efficiency_consultants', 'pipeline_operators', 'meter_readers', 'wastewater_treatment_technicians', 'electrical_engineers', 'environmental_compliance_specialists', 'utility_inspectors', 'field_service_technicians', 'telecom_power_technicians', 'nuclear_plant_operators', 'hydropower_technicians', 'solar_panel_installers']
    overview: str | None = Field(max_length=1500)
    job_description: str = Field(3000)
    experience: Literal["fresher", "no_experience", "expert", "internship", "intermediate"]
    responsibility: str | None = Field(max_length=2000)
    required_skills: str | None = Field(500)
    benefits: str | None = Field(1500)
    job_url: str | None = Field(100)

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "job_type": "full_time",
                    "job_title": "Software Engineer",
                    "location": {
                        "country": "united kingdom",
                        "state": "greater manchester"
                    },
                    "salary_amount": 7500.00,
                    "salary_duration": "monthly",
                    "category": "engineering",
                    "sub_category": "software_engineers",
                    "experience": "fresher",
                    "overview": "This is a great opportunity for a software engineer.",
                    "job_description": "Responsible for developing and maintaining software applications.",
                    "responsibility": "Write clean, maintainable code.",
                    "required_skills": "Python, JavaScript, SQL",
                    "benefits": "Healthcare, 401(k), flexible hours",
                    "job_url": "https://hellojob24.com/todays/job/234234/getsoftwarejob/noapplicaton/2"
                }
            ]
        }
    }


# PYDANTIC CLASS FOR COVER LETTER
class CoverModel(BaseModel):
    title: str = Field(max_length=300)
    letter: str | None = Field(max_length=1000)


# PYDANTIC CLASS FOR JOB APPLICATION
class ApplicationModel(BaseModel):
    # application_id: str = Field(max_length=15)
    job_id: str = Field(max_length=50)
    cover_letter: CoverModel
    
    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "job_id": "enter job_id",
                    "cover_letter": {
                        "title": "Apply as an Software Engineer at Pepsico with 2 years working experience",
                        "cover_letter": "I am writing to express my interest in the Software Engineer position at PepsiCo. I have been following PepsiCo's work for some time now, and I am very impressed with the company's commitment to innovation and its use of technology to improve the lives of its customers. I believe that my skills and experience would be a valuable asset to your team, and I am eager to contribute to PepsiCo's continued success. I have 6 years of experience in software engineering, with a focus on developing and maintaining web applications and mobile apps. I have a strong understanding of software development best practices, including object-oriented programming, design patterns, and unit testing. I am also proficient in a variety of programming languages and technologies, including Java, Python, JavaScript, React Native, and AWS."
                    }
                }
            ]
        }
    }


# PYDANTIC CLASS FOR JOB RESPONSE MODEL
# class JobResponseModel(BaseModel):
#     id: int
#     name_id: str
#     company: str
#     job_type: Literal["fixed_price", "full_time", "part_time", "freelance"]
#     posted_on: datetime
#     job_title: str
#     location: LocationModel | None = None
#     salary_amount: float | None = None
#     salary_duration: str
#     experience: str
#     overview: str | None = None
#     job_description: str
#     category: str
#     responsibility: str | None = None
#     required_skills: str | None = None
#     benefits: str | None = None
#     job_url: str | None = None


