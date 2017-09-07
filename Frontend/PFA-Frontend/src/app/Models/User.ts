export class User {
  firstName: string;
  lastName: string;
  email: string;
  age: number;

  constructor(userInfo: any) {
    this.firstName = userInfo.firstName;
    this.lastName = userInfo.lastName;
    this.email = userInfo.email;
    this.age = userInfo.age;
  }
}
