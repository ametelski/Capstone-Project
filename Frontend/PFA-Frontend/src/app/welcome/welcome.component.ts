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
      uri: '/pythonSkillTree',
      usersProgress: 20
    },
    {
      skillName: 'HTML',
      uri: '/HTMLSkillTree',
      usersProgress: 45
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
