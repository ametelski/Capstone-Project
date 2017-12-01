export interface ISkillConcept {
// skillConceptName: String
// skillDescription: String
// extLearnLinks: String[]
// completed: boolean
// location: Number

_id: String
description: String
extLearnLinks: String[]
id: Number
location: String
skillConceptName: String
isCompleted?: Boolean
}

export interface ISkillConceptRootObject {
  skillConcepts: ISkillConcept[];
}

export interface ISkillConceptsIds {
  skillConceptsIds: number[];
}
