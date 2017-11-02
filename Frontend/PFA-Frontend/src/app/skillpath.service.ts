import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { ISkillPath } from './Models/skillPath.model';
import {Observable} from 'rxjs/RX'

@Injectable()
export class SkillpathService {

  constructor(private http: Http) { }

  getSkillPath(): Observable <ISkillPath[]> {
    return this.http.get('http://127.0.0.1:5000/getSkill?studentID=1').map(res => res.json());
  }
}
