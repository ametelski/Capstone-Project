import { ISkillConcept } from './skillConcept.model';

export interface ISkills {
  skillName: string;
  completed?: Number;
}

export interface ISkillRootObject {
  skills: ISkills[];
}
