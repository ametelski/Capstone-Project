import { ISkillConcept } from './skillConcept.model';
export interface ISkill {
  skillName: string
  skillConceptCompleted: number
  skillURL?: string
  skillConcepts: ISkillConcept[]
}
