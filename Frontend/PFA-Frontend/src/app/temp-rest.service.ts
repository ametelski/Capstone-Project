import {Http} from '@angular/http';
import { Injectable } from '@angular/core';
import 'rxjs/add/operator/map'

@Injectable()
export class TempRestService {

  constructor(private http: Http ) { }

  getService() {
    return this.http.get('http://localhost:8080/greeting').map(res => res.json());
  }
}
