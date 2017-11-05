import { ISkillConcept } from './skillConcept.model';
export interface ISkillPath {
  skillName: string
  skillConceptCompleted: number
  skillURL?: string
  skillConcepts: ISkillConcept[]
}
