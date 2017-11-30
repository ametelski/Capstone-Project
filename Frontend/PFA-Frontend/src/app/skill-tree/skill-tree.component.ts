import { Component, OnInit, Input } from '@angular/core';
import { SkillpathService } from '../skillpath.service';
import { ISkills, ISkillRootObject } from '../Models/skillPath.model';
import { ISkillConcept, ISkillConceptsIds } from '../Models/skillConcept.model';


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
  skConIDS: ISkillConceptsIds
  name: String = 'Scratch'
  title: String
  description: String
  extLearnLinks: String[]
  showPassword: Boolean =  false;
  isCompleted: Boolean[] = [false, false, false, false, false, false, false, false]

  constructor(private service: SkillpathService) {}

  ngOnInit() {
    this.getSkillTreeConcepts();
    //this.getStudentsCompletedSkill()
  }


  markSkillConceptsCompleted() {
    debugger
    for (let i = 0; i < this.skillConcepts.length; i++ ) {
      for (let j = 0; j < this.skConIDS.skillConceptsIds.length; j++) {
        if (this.skillConcepts[i].id === this.skConIDS.skillConceptsIds[j]) {
          this.skillConcepts[i].isCompleted = true;
          this.isCompleted[i] = true;
        }
      }
      if (!this.skillConcepts[i].isCompleted) {
        this.skillConcepts[i].isCompleted = false;
      }
    }
  }


  getStudentsCompletedSkill() {
    this.service.getArrayOfSkillConceptsIdStudentHasCompleted(1).subscribe(data => {
      //debugger;
      this.skConIDS = data;
      console.log(this.skConIDS);
      this. markSkillConceptsCompleted()
     });
  }
  getSkillTreeConcepts() {
    this.service.getSkillConceptsByName('Scratch').subscribe(data => {
     // debugger;
      this.skillConcepts = data.skillConcepts;
      console.log(data.skillConcepts);
      this.getStudentsCompletedSkill();
     })
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

 closeModal(element) {
  element.hide()
  this.showPassword = false;
 }
  checkPassword(password, element) {
      if (password.value === '1234') {
        // make service call
        password.value = null
        this.showPassword = false;
        element.hide()
        this.isCompleted[this.selector] = true;
      }
  }
}
