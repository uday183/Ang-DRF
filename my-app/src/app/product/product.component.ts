import { Component, OnInit, ViewChild } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';
declare var $: any;

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})

export class ProductComponent implements OnInit {
  @ViewChild('closebutton') closebutton;
  dtOptions: DataTables.Settings = {};
  showContent: boolean;
  constructor(
    private apiService: ApiService,
    private router: Router,
    ) { }
  product;
  image;
  userpersonal;
  username = '';
  city = '';
  country = '';
  id = '';
  item: any;
  spinnerFlag = true;

  // tslint:disable-next-line:typedef
  ngOnInit(){
   this.getUsers();
   this.getPersonal();
   this.dtOptions = {
    pagingType: 'full_numbers',
    pageLength: 5,
    processing: true,
  };
   setTimeout(() => this.showContent = true, 250);
}
  // tslint:disable-next-line:typedef
  getUsers(){
    this.spinnerFlag = true;
    this.apiService.getTasks().subscribe((result: any) => {
    // console.log("Result ===>",result);
    this.product = result.data;
    this.image = result.data[0].profile_image;

    console.log(result.data[0].profile_image);
    this.spinnerFlag = false;
   });
  }
  // tslint:disable-next-line:typedef
  getPersonal(){
    this.apiService.getPersonalInfo().subscribe((result: any) => {
      // console.log("Result ===>",result);
      this.userpersonal = result.data;
     });

  }
  // tslint:disable-next-line:typedef
  logouts(){
    // this.router.navigate(['/']);
    this.apiService.Logout().subscribe((result: any) => {
        this.router.navigate(['/']);
     });


  }

  create(): void{

    this.apiService.UserCreate(this.username, this.city, this.country, this.id ).subscribe((result: any) => {
    $('#basicExampleModal').modal('hide');
    this.getUsers();
     });

  }

  delete(id): void{
    console.log(id);
    this.apiService.UserDelete(id).subscribe((result: any) => {
    this.getUsers();
     });

  }

  edit(item: any): void{
    this.id = item.id;
    this.username = item.name;
    this.city = item.city;
    this.country = item.country;
  }

  clear(): void{
    this.id = '';
    this.username = '';
    this.city = '';
    this.country = '';
  }
 }
