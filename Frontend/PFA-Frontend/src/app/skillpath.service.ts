import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { ISkill } from './Models/skillPath.model';
import {Observable} from 'rxjs/RX'
import {SKILL} from './mock-Skills'
import { of } from 'rxjs/observable/of';

@Injectable()
export class SkillpathService {

  constructor(private http: Http) { }

  // Mock get Skill
  getSkill(): Observable<ISkill[]> {
    return of(SKILL);
  }

  // getSkill(): Observable <ISkill[]> {
  //   return this.http.get('http://127.0.0.1:5000/getSkill?studentID=1')
  //                   .map((response: Response) => {

  //                     return <ISkill[]>response.json()
  //                   }).catch(this.handleError);
  // }

  private handleError(error: Response) {
      return Observable.throw(error.statusText)
  }

}
