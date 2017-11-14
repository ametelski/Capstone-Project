<h1>Programming For All Project Documentation</h1>
<h6>Author: Miguel Deniz & Nguyen Dao</h6>
<h6>Last Update: 10/3/17</h6>

<h6>Swagger Version: https://app.swaggerhub.com/apis/ngdao/Capstone/1.0.0<h6>

<h2>RESTful Service Calls</h2>
<h4>getSkill</h4>

```
Description:
    Returns a list of all skills and their statuses for a specific user.

Sample URL:
    "http://127.0.0.1:5000/students/<int:studentID>/skills

Parameters:
    studentID

Returns:
    JSON
        
Example Return:
{
  "skills": [
        {
            "completedPercentage": 100,
            "name": "HTML",
            "skillConcepts": [
                {
                    "completed": true,
                    "description": "to help kids with...",
                    "extLearnLinks": [
                        "www.link1.com",
                        "www.link2.com"
                    ],
                    "id": 1,
                    "location": "R1C2",
                    "skillConceptName": "Repetition"
                },
                {
                    "completed": true,
                    "description": "Student Has COMPLETED this MODULE...",
                    "extLearnLinks": [
                        "www.link1.com",
                        "www.link2.com"
                    ],
                    "id": 2,
                    "location": "R2C1",
                    "skillConceptName": "Condition"
                },
                {
                    "completed": true,
                    "description": "to help kids with...",
                    "extLearnLinks": [
                        "www.link1.com",
                        "www.link2.com"
                    ],
                    "id": 3,
                    "location": "R2C3",
                    "skillConceptName": "Procedural"
                }
            ],
            "url": "www.linkToTheTree.com"
        },
        {
            "completedPercentage": 0,
            "name": "Python",
            "skillConcepts": [
                {
                    "completed": false,
                    "description": "to help kids with...",
                    "extLearnLinks": [
                        "www.link1.com",
                        "www.link2.com"
                    ],
                    "id": 1,
                    "location": "R1C2",
                    "skillConceptName": "Repetition"
                },
                {
                    "completed": false,
                    "description": "Student Has COMPLETED this MODULE...",
                    "extLearnLinks": [
                        "www.link1.com",
                        "www.link2.com"
                    ],
                    "id": 2,
                    "location": "R2C1",
                    "skillConceptName": "Condition"
                },
                {
                    "completed": false,
                    "description": "to help kids with...",
                    "extLearnLinks": [
                        "www.link1.com",
                        "www.link2.com"
                    ],
                    "id": 3,
                    "location": "R2C3",
                    "skillConceptName": "Procedural"
                }
            ],
            "url": "www.linkToTheTree.com"
        },
    ...
    ]
``` 

<h4>getSkillConcept</h4>

```
Description:
    Returns the skill concepts for a specific userID and skillType

Sample URL:
    http://127.0.0.1:5000/getSkillConcept?userID=USER_ID&skillType=SKILL_TYPE

Params:
    userID, skillType
    
Returns:
    JSON

Example:
    {
      "completed": true, 
      "extLearnLinks": "www.google.com,www.bing.com,www.ask.com", 
      "location": "1,2", 
      "skillDescription": "Python skill concepts", 
      "skillTitle": "Python"
    }
```

