export interface ISkillConcept {

_id: String
description: String
extLearnLinks: ExtLearnLink[]
id: Number
location: String
skillConceptName: String
isCompleted?: Boolean
}
export interface ExtLearnLink {
  shortName: string;
  url: string;
}

export interface ISkillConceptRootObject {
  skillConcepts: ISkillConcept[];
}

export interface ISkillConceptsIds {
  skillConceptsIds: number[];
}
