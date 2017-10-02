import {Routes} from '@angular/router';
import { SignUpComponent } from './app/sign-up/sign-up.component';
import { WelcomeComponent } from './app/welcome/welcome.component';
import { UserRoleComponent } from './app/user-role/user-role.component';


export const appRoutes: Routes = [
  {path: 'sign-up', component: SignUpComponent},
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'welcome', component: WelcomeComponent},
  {path: 'user-role', component: UserRoleComponent}
]
