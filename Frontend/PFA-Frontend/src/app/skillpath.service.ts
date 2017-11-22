import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import {ISkillRootObject } from './Models/skillPath.model';
import {Observable} from 'rxjs/RX'

import { of } from 'rxjs/observable/of';
import { ISkillConcept, ISkillConceptRootObject } from 'app/Models/skillConcept.model';

@Injectable()
export class SkillpathService {

  constructor(private http: Http) { }

  private handleError(error: Response) {
      return Observable.throw(error.statusText)
  }

/*
  -----------------------------------------------------------------------------------------------
  Get all skill concepts that belong to a skill(tree) by name [/skills/<skillName>/skillConcepts]
  -----------------------------------------------------------------------------------------------
  Example endpoint: http://127.0.0.1:5000/skills/Scratch/skillConcepts
*/

  getSkillConceptsByName(skillName): Observable <ISkillConceptRootObject> {
    return this.http.get('http://127.0.0.1:5000/skills/' + skillName + '/skillConcepts')
                    .map((response: Response) => {
debugger
                      return <ISkillConceptRootObject>response.json()
                    }).catch(this.handleError);
  }
/*
-----------------------------------------------------------------------------------------------
Get array of skillConcept IDs that belong to a skill(tree) by name [/skills/<skillName>/skillConceptId]
-----------------------------------------------------------------------------------------------
Example endpoint: http://127.0.0.1:5000/skills/Scratch/skillConceptsIds

*/
getSkillConceptsIdByName(skillName): Observable <Number[]> {
  return this.http.get('http://127.0.0.1:5000/skills/' + skillName + '/skillConceptsIds')
                  .map((response: Response) => {
                    return <Number[]>response.json()
                  }).catch(this.handleError);
}

/*
-----------------------------------------------------------------------------------------------
Get the skillName of all the skills a student belongs to:
-----------------------------------------------------------------------------------------------
Example endpoint: http://127.0.0.1:5000/students/1/skills

*/
getSkillsByStudentId(studentID): Observable <ISkillRootObject> {
  return this.http.get('http://127.0.0.1:5000/students/' + studentID + '/skills')
                  .map((response: Response) => {
                    return <ISkillRootObject>response.json()
                  }).catch(this.handleError);
}

/*
-----------------------------------------------------------------------------------------------
Get all the data for a skill concept by its ID
-----------------------------------------------------------------------------------------------
Example endpoint: http://127.0.0.1:5000/skillConcepts/2

*/
getAllDataForSkillConceptById(skillConceptID): Observable <ISkillConcept> {
  return this.http.get('http://127.0.0.1:5000/skillConcepts/' + skillConceptID)
                  .map((response: Response) => {
                    return <ISkillConcept>response.json()
                  }).catch(this.handleError);
}

/*
-----------------------------------------------------------------------------------------------
Get array of skillConcepts a student has completed
-----------------------------------------------------------------------------------------------
Example endpoint: http://127.0.0.1:5000/students/1/skillConcepts/completed

*/
getArrayOfSkillConceptsStudentHasCompleted(studentID): Observable <ISkillConcept[]> {
  return this.http.get('http://127.0.0.1:5000/students/' + studentID + '/skillConcepts/completed')
                  .map((response: Response) => {
                    return <ISkillConcept[]>response.json()
                  }).catch(this.handleError);
}
/*
-----------------------------------------------------------------------------------------------
Get array of skillConcept Id's that a student has completed
-----------------------------------------------------------------------------------------------
Example endpoint: http://127.0.0.1:5000/students/1/skillConcepts/completedIds

*/

getArrayOfSkillConceptsIdStudentHasCompleted(studentID): Observable <any[]> {
  return this.http.get('http://127.0.0.1:5000/students/' + studentID + '/skillConcepts/completedIds')
                  .map((response: Response) => {
                    return <any[]>response.json()
                  }).catch(this.handleError);
}



}
