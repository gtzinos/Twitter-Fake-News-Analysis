import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ChartElementComponent } from './chart-element.component';

describe('ChartElementComponent', () => {
  let component: ChartElementComponent;
  let fixture: ComponentFixture<ChartElementComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChartElementComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChartElementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
