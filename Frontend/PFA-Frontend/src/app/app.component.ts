import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class = "grid-container" >
      <app-navbar></app-navbar>
      <router-outlet></router-outlet>
    </div>
    `
})
export class AppComponent {
  title = 'Programming for All';
}
