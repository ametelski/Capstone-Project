import { ISkillConcept } from './skillConcept.model';

export interface ISkills {
  skillName: string;
}

export interface ISkillRootObject {
  skills: ISkills[];
}
