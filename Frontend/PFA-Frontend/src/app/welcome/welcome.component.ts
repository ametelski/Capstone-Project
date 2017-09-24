import { Component, OnInit } from '@angular/core';
import { TempRestService } from '../temp-rest.service';
import { ISkillPath } from '../Models/skillPath.model';

@Component({
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  skillPath: ISkillPath[] = [
    {
      skillName: 'Python',
      URL: '/sign-up',
      usersProgress: 20
    },
    {
      skillName: 'HTML',
      URL: '/HTMLSkillTree',
      usersProgress: 45
    },
    {
    skillName: 'Scratch',
    URL: '/ScatchConcepts',
    usersProgress: 95
    }

  ]


  id
  content: string[]
  data: JSON

  constructor(private service: TempRestService) { }


  ngOnInit() {
     this.service.getService().subscribe(data => {
      this.data = data;
      console.log(data);
      this.id = data['id'];
      this.content = data['content']
     });
  }



}
