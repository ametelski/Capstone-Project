import { ISkill } from './Models/skillPath.model';

export const SKILL: ISkill[] = [
  {
    skillName: 'Scratch',
    skillURL: '/ScatchConcepts',
    skillConceptCompleted: 95,
    skillConcepts: [
      {
        skillConceptName: 'Sequencing',
        skillDescription: 'This area will contain sequencing the detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
        completed: false,
        location: 2.2
      },
      {
        skillConceptName: 'Repitition',
        skillDescription: 'This area will contain repitition detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
        completed: false,
        location: 2.2
      },
      {
        skillConceptName: 'Variables',
        skillDescription: 'This area will contain variables detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
        completed: false,
        location: 2.2
      },
      {
        skillConceptName: 'Boolean Operation',
        skillDescription: 'This area will contain boolean operation detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
        completed: false,
        location: 2.2
      },
      {
        skillConceptName: 'Data Structure',
        skillDescription: 'This area will contain data structure detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
        completed: false,
        location: 2.2
      },
      {
        skillConceptName: 'Functions',
        skillDescription: 'This area will contain functions detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
        completed: false,
        location: 2.2
      },
      {
        skillConceptName: 'Project Management',
        skillDescription: 'This area will contain project management detailed description',
        extLearnLinks: ['www.google.com', 'www.code.com'],
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
