import { Component, OnInit } from '@angular/core';
import { TempRestService } from '../temp-rest.service';
import { ISkillRootObject, ISkills } from '../Models/skillPath.model';
import { SkillpathService } from '../skillpath.service';

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



}
