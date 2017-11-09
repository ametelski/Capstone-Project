import { Component, OnInit, Input } from '@angular/core';
import { SkillpathService } from '../skillpath.service';
import { ISkillPath } from '../Models/skillPath.model';
import { ISkillConcept } from '../Models/skillConcept.model';

@Component({
  selector: 'app-skill-tree',
  templateUrl: './skill-tree.component.html',
  styleUrls: ['./skill-tree.component.css']
})
export class SkillTreeComponent implements OnInit {
  @Input() skill: String;

  skillConcepts: ISkillConcept[] = [
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
  ];

  constructor(private service: SkillpathService) {}

  ngOnInit() {
    this.getSkillTreeConcepts();
  }

  getSkillTreeConcepts() {
    this.service.getSkillPath().subscribe(data => {
      debugger;
      // this.skillConcept = data[0].skillConcepts
      console.log(data[0]);
    });
  }

  getName(num) {
    return this.skillConcepts[num].skillConceptName;
  }

  getDescription(num) {
    return this.skillConcepts[num].skillDescription;
  }

  getExternalLinks(num) {
    return this.skillConcepts[num].extLearnLinks;
  }

  getCompletion(num) {
    return this.skillConcepts[num].completed;
  }
}
