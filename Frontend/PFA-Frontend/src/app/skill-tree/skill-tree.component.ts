import { Component, OnInit, Input } from '@angular/core';
import { SkillpathService } from '../skillpath.service';
import { ISkills, ISkillRootObject } from '../Models/skillPath.model';
import { ISkillConcept } from '../Models/skillConcept.model';


@Component({
  selector: 'app-skill-tree',
  templateUrl: './skill-tree.component.html',
  styleUrls: ['./skill-tree.component.css']
})
export class SkillTreeComponent implements OnInit {
  @Input() skill: String;
  // the selector variable will be used to select array elements
  selector = 0

  skillConcepts: ISkillConcept[]
  name: String = 'Scratch'
  title: String
  description: String
  extLearnLinks: String[]

  constructor(private service: SkillpathService) {}

  ngOnInit() {
    this.getSkillTreeConcepts();
  }
  getSkillTreeConcepts() {
    this.service.getSkillConceptsByName('Scratch').subscribe(data => {
      debugger;
      this.skillConcepts = data.skillConcepts;
      console.log(data.skillConcepts.length);
     });
  }

  buttonClicked(num, elemt) {
    debugger
    this.selector = num
    this.title = this.skillConcepts[this.selector].skillConceptName
    this.description = this.skillConcepts[this.selector].description;
    this.extLearnLinks = this.skillConcepts[this.selector].extLearnLinks
    elemt.show()
  }

  getName() {
    return this.skillConcepts[this.selector].skillConceptName
  }

  getDescription() {
    return this.skillConcepts[this.selector].description;
  }

  getExternalLinks() {
    return this.skillConcepts[this.selector].extLearnLinks;
  }

  // getCompletion(num) {
  //   return this.skillConcepts[this.selector].completed;
  // }
}
