"""
Medical information database for heart conditions
"""

def get_disease_info(condition):
    """Get detailed information about a heart condition"""
    
    disease_info = {
        'coronary_artery_disease': {
            'name': 'Coronary Artery Disease (CAD)',
            'description': 'A condition where the coronary arteries become narrowed or blocked due to plaque buildup, reducing blood flow to the heart muscle.',
            'symptoms': [
                'Chest pain or discomfort (angina)',
                'Shortness of breath',
                'Fatigue during physical activity',
                'Heart palpitations',
                'Nausea or dizziness'
            ],
            'causes': [
                'High cholesterol levels',
                'High blood pressure',
                'Smoking',
                'Diabetes',
                'Family history of heart disease',
                'Sedentary lifestyle',
                'Obesity'
            ],
            'complications': [
                'Heart attack (myocardial infarction)',
                'Heart failure',
                'Irregular heart rhythms',
                'Sudden cardiac death'
            ]
        },
        
        'arrhythmia': {
            'name': 'Heart Arrhythmia',
            'description': 'An irregular heartbeat that occurs when the electrical impulses that coordinate heartbeats don\'t work properly.',
            'symptoms': [
                'Heart palpitations',
                'Rapid or slow heartbeat',
                'Chest pain',
                'Shortness of breath',
                'Dizziness or lightheadedness',
                'Fainting or near-fainting'
            ],
            'causes': [
                'Heart disease',
                'High blood pressure',
                'Diabetes',
                'Smoking',
                'Excessive alcohol or caffeine',
                'Stress',
                'Certain medications'
            ],
            'complications': [
                'Stroke',
                'Heart failure',
                'Sudden cardiac arrest',
                'Blood clots'
            ]
        },
        
        'heart_failure': {
            'name': 'Heart Failure',
            'description': 'A condition where the heart cannot pump blood effectively to meet the body\'s needs for blood and oxygen.',
            'symptoms': [
                'Shortness of breath',
                'Fatigue and weakness',
                'Swelling in legs, ankles, and feet',
                'Rapid or irregular heartbeat',
                'Persistent cough with white or pink phlegm',
                'Sudden weight gain'
            ],
            'causes': [
                'Coronary artery disease',
                'High blood pressure',
                'Heart attack',
                'Cardiomyopathy',
                'Heart valve disease',
                'Diabetes'
            ],
            'complications': [
                'Kidney damage',
                'Liver damage',
                'Malnutrition',
                'Pulmonary edema',
                'Sudden cardiac death'
            ]
        },
        
        'valve_disease': {
            'name': 'Heart Valve Disease',
            'description': 'A condition where one or more heart valves don\'t work properly, affecting blood flow through the heart.',
            'symptoms': [
                'Shortness of breath',
                'Chest pain',
                'Fatigue',
                'Dizziness or fainting',
                'Heart palpitations',
                'Swelling in ankles or feet'
            ],
            'causes': [
                'Congenital heart defects',
                'Rheumatic fever',
                'Infections',
                'Age-related wear and tear',
                'High blood pressure',
                'Heart attack'
            ],
            'complications': [
                'Heart failure',
                'Stroke',
                'Blood clots',
                'Irregular heart rhythms',
                'Sudden cardiac death'
            ]
        },
        
        'cardiomyopathy': {
            'name': 'Cardiomyopathy',
            'description': 'A disease of the heart muscle that makes it harder for the heart to pump blood to the rest of the body.',
            'symptoms': [
                'Shortness of breath',
                'Fatigue',
                'Swelling in legs and feet',
                'Irregular heartbeat',
                'Dizziness or lightheadedness',
                'Chest pain'
            ],
            'causes': [
                'Genetic factors',
                'High blood pressure',
                'Heart attacks',
                'Viral infections',
                'Alcohol abuse',
                'Chemotherapy drugs'
            ],
            'complications': [
                'Heart failure',
                'Blood clots',
                'Heart valve problems',
                'Sudden cardiac arrest'
            ]
        },
        
        'hypertension': {
            'name': 'Hypertension (High Blood Pressure)',
            'description': 'A condition where blood pressure in the arteries is persistently elevated, forcing the heart to work harder.',
            'symptoms': [
                'Often no symptoms (silent killer)',
                'Headaches',
                'Shortness of breath',
                'Chest pain',
                'Dizziness',
                'Nosebleeds'
            ],
            'causes': [
                'Unhealthy diet (high sodium)',
                'Lack of physical activity',
                'Obesity',
                'Smoking',
                'Excessive alcohol consumption',
                'Stress',
                'Family history'
            ],
            'complications': [
                'Heart attack',
                'Stroke',
                'Heart failure',
                'Kidney disease',
                'Vision problems'
            ]
        }
    }
    
    return disease_info.get(condition, {
        'name': condition.replace('_', ' ').title(),
        'description': 'Heart condition requiring medical attention.',
        'symptoms': ['Consult with healthcare provider for symptom information'],
        'causes': ['Multiple factors may contribute to this condition'],
        'complications': ['Potential complications should be discussed with a doctor']
    })

def get_health_tips(condition, form_data):
    """Get personalized health tips based on condition and patient data"""
    
    general_tips = [
        "Maintain a healthy weight and BMI",
        "Exercise regularly (at least 150 minutes of moderate activity per week)",
        "Follow a heart-healthy diet",
        "Quit smoking and avoid secondhand smoke",
        "Limit alcohol consumption",
        "Manage stress through relaxation techniques",
        "Get adequate sleep (7-9 hours per night)",
        "Monitor blood pressure regularly",
        "Take medications as prescribed by your doctor"
    ]
    
    condition_specific_tips = {
        'coronary_artery_disease': [
            "Monitor cholesterol levels regularly",
            "Control blood sugar if diabetic",
            "Consider cardiac rehabilitation programs",
            "Learn to recognize signs of heart attack"
        ],
        'arrhythmia': [
            "Avoid excessive caffeine and stimulants",
            "Practice stress management techniques",
            "Monitor heart rate regularly",
            "Avoid triggers that cause irregular heartbeat"
        ],
        'heart_failure': [
            "Monitor daily weight for sudden changes",
            "Limit sodium intake to less than 2,300mg per day",
            "Monitor fluid intake as recommended by doctor",
            "Elevate legs when resting to reduce swelling"
        ],
        'valve_disease': [
            "Follow antibiotic prophylaxis if recommended",
            "Inform dentist and doctors about valve condition",
            "Monitor for signs of infection",
            "Regular echocardiograms as recommended"
        ],
        'cardiomyopathy': [
            "Avoid alcohol completely if alcohol-induced",
            "Monitor for signs of heart failure",
            "Consider genetic counseling if hereditary",
            "Regular monitoring with cardiologist"
        ],
        'hypertension': [
            "Check blood pressure regularly at home",
            "Reduce sodium intake significantly",
            "Increase potassium-rich foods",
            "Practice meditation or deep breathing exercises"
        ]
    }
    
    # Add personalized tips based on form data
    personalized_tips = []
    
    # Age-specific tips
    age = form_data.get('age')
    if age and age > 65:
        personalized_tips.append("Regular health screenings are especially important at your age")
    
    # BMI-specific tips
    bmi = form_data.get('bmi')
    if bmi and bmi > 30:
        personalized_tips.append("Weight management is crucial - consider consulting a nutritionist")
    elif bmi and bmi < 18.5:
        personalized_tips.append("Maintain adequate nutrition to support heart health")
    
    # Smoking-specific tips
    if form_data.get('smoking') == 1:
        personalized_tips.append("Quitting smoking is the single most important step for your heart health")
    
    # Stress-specific tips
    stress_level = form_data.get('stress_level')
    if stress_level and stress_level > 7:
        personalized_tips.append("High stress levels require immediate attention - consider counseling or stress management programs")
    
    # Physical activity tips
    activity_level = form_data.get('physical_activity')
    if activity_level and activity_level < 3:
        personalized_tips.append("Gradually increase physical activity with your doctor's guidance")
    
    # Combine all tips
    all_tips = general_tips + condition_specific_tips.get(condition, []) + personalized_tips
    
    return all_tips[:8]  # Return top 8 most relevant tips

def get_diet_recommendations(condition, form_data):
    """Get personalized diet recommendations based on condition and patient data"""
    
    general_recommendations = {
        'foods_to_include': [
            "Fatty fish (salmon, mackerel, sardines) - 2-3 times per week",
            "Leafy green vegetables (spinach, kale, collard greens)",
            "Whole grains (oats, brown rice, quinoa)",
            "Berries and other antioxidant-rich fruits",
            "Nuts and seeds (almonds, walnuts, flaxseeds)",
            "Legumes (beans, lentils, chickpeas)",
            "Avocados and olive oil",
            "Low-fat dairy or plant-based alternatives"
        ],
        'foods_to_limit': [
            "Processed and packaged foods high in sodium",
            "Red meat and processed meats",
            "Sugary drinks and desserts",
            "Trans fats and saturated fats",
            "Refined grains and white bread",
            "Excessive alcohol",
            "High-sodium condiments and sauces"
        ]
    }
    
    condition_specific = {
        'coronary_artery_disease': {
            'focus': 'Lower cholesterol and reduce inflammation',
            'special_foods': [
                "Oatmeal with soluble fiber",
                "Plant sterols and stanols",
                "Soy protein foods",
                "Green tea"
            ],
            'avoid': [
                "Foods high in saturated fat",
                "Trans fats",
                "Excess dietary cholesterol"
            ]
        },
        'hypertension': {
            'focus': 'Reduce sodium and increase potassium',
            'special_foods': [
                "Bananas and potassium-rich fruits",
                "Dark chocolate (in moderation)",
                "Beets and beet juice",
                "Garlic and herbs for flavoring"
            ],
            'avoid': [
                "High-sodium processed foods",
                "Canned soups with added salt",
                "Pickled foods",
                "Restaurant and fast foods"
            ]
        },
        'heart_failure': {
            'focus': 'Manage fluid retention and sodium',
            'special_foods': [
                "Fresh fruits and vegetables",
                "Lean proteins",
                "Herbs and spices for flavor"
            ],
            'avoid': [
                "Excessive fluids if restricted",
                "High-sodium foods",
                "Canned vegetables with added salt"
            ]
        },
        'arrhythmia': {
            'focus': 'Avoid triggers and maintain electrolyte balance',
            'special_foods': [
                "Magnesium-rich foods (dark chocolate, nuts)",
                "Potassium-rich foods",
                "Omega-3 fatty acids"
            ],
            'avoid': [
                "Excessive caffeine",
                "Energy drinks",
                "Large meals",
                "Alcohol if it triggers symptoms"
            ]
        }
    }
    
    # Get condition-specific recommendations
    condition_diet = condition_specific.get(condition, {})
    
    # Personalize based on form data
    personalized = {}
    
    # BMI-based recommendations
    bmi = form_data.get('bmi')
    if bmi and bmi > 30:
        personalized['weight_management'] = [
            "Focus on portion control",
            "Increase fiber intake to feel full",
            "Choose nutrient-dense, low-calorie foods",
            "Consider consulting a registered dietitian"
        ]
    
    # Diabetes considerations
    if form_data.get('diabetes') == 1:
        personalized['diabetes_friendly'] = [
            "Choose complex carbohydrates",
            "Monitor blood sugar regularly",
            "Include protein with each meal",
            "Limit simple sugars and refined carbs"
        ]
    
    # Age considerations
    age = form_data.get('age')
    if age and age > 65:
        personalized['senior_nutrition'] = [
            "Ensure adequate protein intake",
            "Consider vitamin D and B12 supplements",
            "Stay hydrated",
            "Choose foods easy to chew and digest"
        ]
    
    return {
        'general': general_recommendations,
        'condition_specific': condition_diet,
        'personalized': personalized,
        'meal_planning_tips': [
            "Plan meals in advance",
            "Cook at home more often",
            "Read nutrition labels carefully",
            "Use herbs and spices instead of salt",
            "Eat regular, balanced meals",
            "Stay hydrated with water"
        ]
    }
