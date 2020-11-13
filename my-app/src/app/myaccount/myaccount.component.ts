import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-myaccount',
  templateUrl: './myaccount.component.html',
  styleUrls: ['./myaccount.component.css']
})
export class MyaccountComponent implements OnInit {

  constructor(
    private router: Router,
    private apiService: ApiService
  ) { }
  userdata = [];
  userid ;
  useraccount = [];
  follwerscount ;
  followingcount ;
  postcount ;
  postid ;
  usersfollowers = [];
  userfollowing = [];
  isDisplayModal ;
  likeduserslist = [];
  likedFlag ;
  DisplayModal ;
  ngOnInit(): void {
    this.userData();
    this.user_account();
  }

  userData(): void{
    this.userid = sessionStorage.getItem('user_id');
    this.apiService.userInfo(this.userid).subscribe((result: any) => {
      this.userdata = result.data;
      console.log('login userdata ===>', this.userdata);
     });

  }

  user_account(): void{
    this.apiService.userAccount(this.userid).subscribe((result: any) => {
      this.useraccount = result.data;
      this.followingcount = result.following_count;
      this.follwerscount = result.follwers_count;
      this.postcount = result.post_count;
      console.log('user_account ===>', this.useraccount);
     });
  }

  userfollowers(): void{
    this.isDisplayModal = true;
    this.apiService.userFollowers(this.userid).subscribe((result: any) => {
      this.usersfollowers = result.data;
      console.log('user_account ===>', this.usersfollowers);
     });
  }

  user_following(): void{
    this.DisplayModal = true;
    this.apiService.userFollowing(this.userid).subscribe((result: any) => {
      this.userfollowing = result.data;
      console.log('user_account ===>', this.userfollowing);
     });
  }

  userliked(postid): void{
    this.likedFlag = true;
    this.apiService.LikedUsers(postid).subscribe((result: any) => {
      this.likeduserslist = result.data;
      console.log('userliked ===>', this.likeduserslist);
     });
  }
  hidemodal(): void{
    this.isDisplayModal = false;
    this.DisplayModal = false;
    this.likedFlag = false;
  }

}
