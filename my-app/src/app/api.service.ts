import { Injectable } from '@angular/core';
import { HttpClient,  HttpRequest, HttpEvent, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Task, UserPersonal } from './task';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  API_URL = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  public getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.API_URL}user_info/`);
  }

  public getPersonalInfo(): Observable<UserPersonal[]> {
    return this.http.get<UserPersonal[]>(`${this.API_URL}user_prsnl_info/`);
  }

  public LoginInfo(loginForm: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}login/`, { loginForm }  );
  }

  public UserCreate(username: any, city: any, country: any, id: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}user_info/`, { username, city , country, id}  );
  }

  public UserDelete(id: number): Observable<any[]>{
    return this.http.delete<any[]>(`${this.API_URL}user_info/` + '?id=' + id );
  }

  public Register(registerForm: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}register/`, { registerForm }  );
  }

  public ForgotPassword(forgotForm: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}forgot_password/`, { forgotForm }  );
  }

  public Logout(): Observable<any[]>{
    return this.http.get<any[]>(`${this.API_URL}logout/`);
  }

  public UserPost(userid: number): Observable<any[]>{
    return this.http.get<any[]>(`${this.API_URL}user_post/` + '?user_id=' + userid);
  }

  public UserComment(postid: any, userid: any, postcomment: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}post_comment/`, {postid, userid, postcomment});
  }

  public GetComment(postid: number): Observable<any[]>{
    return this.http.get<any[]>(`${this.API_URL}get_comment/` + '?post_id=' + postid);
  }

  public UserLiked(postid: any, userid: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}user_like/`, {postid, userid});
  }

  public GetFriends(userid: any): Observable<[]> {
    return this.http.get<[]>(`${this.API_URL}friends/` +  '?userid=' + userid);
  }

  public AllUsers(searchinput: any, userid: any): Observable<[]> {
    return this.http.get<[]>(`${this.API_URL}all_users/` +  '?userid=' + userid + '&searchinput=' + searchinput);
  }
  public FriendReq(receiverid: any, senderid: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}friend_req/`, {receiverid, senderid});
  }
  public FriendAccept(userid: number): Observable<any[]>{
    return this.http.get<any[]>(`${this.API_URL}friend_accept/` + '?userid=' + userid);
  }
  public Accepted(acceptid: any, loginid: any): Observable<any[]>{
    return this.http.post<any[]>(`${this.API_URL}friend_accept/`, {acceptid, loginid});
  }

  public userInfo(userid: number): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.API_URL}userinfo/` + '?userid=' + userid);
  }
  public userAccount(userid: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.API_URL}user_account/` + '?userid=' + userid);
  }
  public userFollowers(userid: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.API_URL}user_fallowers/` + '?userid=' + userid);
  }
  public userFollowing(userid: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.API_URL}user_fallowing/` + '?userid=' + userid);
  }
  public LikedUsers(postid: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.API_URL}liked_users/` + '?postid=' + postid);
  }
  public UserPosts(formData: any): Observable<any[]> {
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'multipart/form-data');
    headers.append('Accept', 'application/json');
    return this.http.post<any[]>(`${this.API_URL}user_post_data/` ,  formData, {headers} );
  }
}





