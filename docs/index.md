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
    "http://127.0.0.1:5000/getSkill?userID=USER_ID"

Parameters:
    userID

Returns:
    JSON
        
Example:
    {
        "skills": [
            {
                "skillConcepts": "concepts", 
                "skillConceptsCompleted": "45", 
                "skillName": "HTML", 
                "skillURL": "www.url0.com"
            }, 
            {
                "skillConcepts": "concepts", 
                "skillConceptsCompleted": "23", 
                "skillName": "Python", 
                "skillURL": "www.url1.com"
            }, 
            {
                "skillConcepts": "concepts", 
                "skillConceptsCompleted": "78", 
                "skillName": "CSS", 
                "skillURL": "www.url2.com"
            }
        ]
    }
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

