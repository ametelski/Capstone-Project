import { Component, OnInit } from '@angular/core';
import { TempRestService } from '../temp-rest.service';
import { ISkill } from '../Models/skillPath.model';
import { SkillpathService } from '../skillpath.service';

@Component({
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  skillPath: ISkill[]

  // = [
  //   {
  //     skillName: 'Python',
  //     URL: '/skillTree',
  //     usersProgress: 20
  //   },
  //   {
  //     skillName: 'HTML',
  //     URL: '/HTMLSkillTree',
  //     usersProgress: 45
  //   },
  //   {
  //   skillName: 'Scratch',
  //   URL: '/ScatchConcepts',
  //   usersProgress: 95
  //   }

  // ]


  id
  content: string[]
  data: JSON

  constructor(private service: SkillpathService) { }


  ngOnInit() {
     this.service.getSkill().subscribe(data => {
      debugger;
      this.skillPath = data;
      console.log(data);
      this.id = data['id'];
      this.content = data['content']
     });
  }



}
