import {Routes} from '@angular/router';
import { SignUpComponent } from './app/sign-up/sign-up.component';
import { WelcomeComponent } from './app/welcome/welcome.component';
import { LoginComponent } from './app/login/login.component';
import { SkillTreeComponent } from './app/skill-tree/skill-tree.component';
import { UserSelectComponent } from './app/user-select/user-select.component';


export const appRoutes: Routes = [
  {path: 'sign-up', component: SignUpComponent},
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'welcome', component: WelcomeComponent},
  {path: 'login', component: LoginComponent},
  {path: 'skillTree', component: SkillTreeComponent},
  {path: 'user-select', component: UserSelectComponent}
]
