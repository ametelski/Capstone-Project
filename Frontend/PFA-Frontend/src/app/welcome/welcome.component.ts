import { Component, OnInit } from '@angular/core';
import { TempRestService } from '../temp-rest.service';
import { ISkillRootObject, ISkills } from '../Models/skillPath.model';
import { SkillpathService } from '../skillpath.service';
import { forEach } from '@angular/router/src/utils/collection';

@Component({
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {

  skillList: ISkillRootObject



  constructor(private service: SkillpathService) { }


  ngOnInit() {
      this.service.getSkillsByStudentId(1).subscribe(data => {
      debugger;
      this.skillList = data;
      console.log(data);
     });


  }


caluclateCompletedSkillConcepts(skill: ISkills) {
//     let totalNumberOfSkillConcepts = 0
//     let studentsCompleted = 0;
//     this.service.getSkillConceptsIdBySkillName(skill.skillName).subscribe(data => {
//         totalNumberOfSkillConcepts = data.skillConceptsIds.length
//     })
//     this.service.getArrayOfSkillConceptsIdStudentHasCompleted(skill.skillName).subscribe(data => {
//       studentsCompleted = data.skillConceptsIds.length
//     })
// debugger
// skill.completed =  studentsCompleted / totalNumberOfSkillConcepts * 1.0
// return studentsCompleted / totalNumberOfSkillConcepts * 1.0
}



}
