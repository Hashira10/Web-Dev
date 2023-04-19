import { Component } from '@angular/core';
import{Company} from "./companies";
import{CompanyService} from "./companies.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'group_app';

  categories: Company[] = [];
  constructor(private categoryService: CompanyService) {
  }
  ngOnInit() {
      this.getCategories();
  }
  getCategories() {
    this.categoryService.getCategories().subscribe((categories) => {
      this.categories = categories;
    });
  }
}
