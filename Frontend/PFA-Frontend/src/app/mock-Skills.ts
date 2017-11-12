import { ISkill } from './Models/skillPath.model';

export const SKILL: ISkill[] = [
  {
    skillName: 'Scratch',
    skillURL: '/ScatchConcepts',
    skillConceptCompleted: 95,
    skillConcepts: [
      {
        skillConceptName: 'Concept 1 name',
        skillDescription: 'This area will contain concepts 1 the detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
        completed: false,
        location: 2.2
      },
      {
        skillConceptName: 'Concept 2 name',
        skillDescription: 'This area will contain concept 2 detailed description',
        extLearnLinks: ['www.link3.com', 'www.link4.com'],
        completed: false,
        location: 2.2
      }
    ]
  },
  {
    skillName: 'Python',
    skillURL: '/skillTree',
    skillConceptCompleted: 20,
    skillConcepts: []
  },
  {
    skillName: 'HTML',
    skillURL: '/HTMLSkillTree',
    skillConceptCompleted: 45,
    skillConcepts: []
  },
];
