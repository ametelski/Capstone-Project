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
}

export interface ISkillConceptRootObject {
  skillConcepts: ISkillConcept[];
}
