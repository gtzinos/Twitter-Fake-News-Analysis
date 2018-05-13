import { ResponsiveTemplateComponent } from './responsive-template.component';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';


describe('ResponsiveTemplateComponent', () => {
  let component: ResponsiveTemplateComponent;
  let fixture: ComponentFixture<ResponsiveTemplateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResponsiveTemplateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResponsiveTemplateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
