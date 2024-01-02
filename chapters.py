from bs4 import BeautifulSoup

html_doc = """
<div class="tutor-accordion-item">
						<h4 class="tutor-accordion-item-header is-active">
							Chapter 1: Introduction &amp; Concepts													</h4>
			
																			<div class="tutor-accordion-item-body" style="">
								<div class="tutor-accordion-item-body-content">
									<ul class="tutor-course-content-list">
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														<a href="https://jiujitsux.com/courses/keenans-lapel-encyclopedia/lesson/1-1-introduction-to-the-lapel-encyclopedia-2/"><span class="lesson-preview-title">1-1 Introduction to the Lapel Encyclopedia</span></a>													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														12:01													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-eye-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														1-2 Course Structure													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														04:20													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														1-3 Gripping Concepts													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														09:04													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														1-4 Intermediary Lapel Control													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														08:54													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														1-5 Avoiding Weak Foot Positioning &amp; Using Lapel Lasso for Control													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														09:32													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														1-6 Finding Lapel Grips Everywhere													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:55													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														1-7 Finding Lapel Grips from More of Everywhere													</h5>
												</div>
												"""
chapter2 = """<div class="tutor-accordion-item">
						<h4 class="tutor-accordion-item-header is-active">
							Chapter 2: Playing Open Guard, Off Balances &amp; Entries													</h4>
			
																			<div class="tutor-accordion-item-body" style="">
								<div class="tutor-accordion-item-body-content">
									<ul class="tutor-course-content-list">
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														<a href="https://jiujitsux.com/courses/keenans-lapel-encyclopedia/lesson/2-1-spider-hook-off-balance-2/"><span class="lesson-preview-title">2-1 Spider Hook Off-Balance</span></a>													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														06:36													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-eye-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-2 Foot Under Off-Balance													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														04:12													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-3 Forward Spider Push to X-Guard													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														08:07													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-4 Forward Spider Push to Crab Ride													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:21													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-5 Forward Spider Push to Single Leg X													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:50													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-6 Foot Under Off Balance to X-Guard													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														04:45													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-7 Foot Under Off-Balance to Calf Slice													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:45													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-8 Foot Under Off-Balance to 50/50													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														04:38													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-9 Foot Under Off-Balance to Squid Guard													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:49													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-10 Belt Guard Control: Gripping Belt Knot													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:02													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														2-11 Belt Guard Control: Gripping Belt Length													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:06													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																			</ul>
								</div>
							</div>
																	</div>
                                                                    """
chapter3 = """<div class="tutor-accordion-item">
						<h4 class="tutor-accordion-item-header is-active">
							Chapter 3: Recovering If Things Go Wrong													</h4>
			
																			<div class="tutor-accordion-item-body" style="">
								<div class="tutor-accordion-item-body-content">
									<ul class="tutor-course-content-list">
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														<a href="https://jiujitsux.com/courses/keenans-lapel-encyclopedia/lesson/3-1-upside-down-spider-kill-technique-2/"><span class="lesson-preview-title">3-1 Upside Down Spider Kill Technique</span></a>													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														07:36													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-eye-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-2 Overhead Leg Swing Recovery Movement													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:47													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-3 Under Leg Swing Recovery Movement													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:08													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-4 Framing With Lapels													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:44													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-5 Avoid Using Your Foot as a Frame When Already Passed													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														02:03													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-6 Avoid Using Your Foot as a Frame When Already Passed Except in this Situation													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														04:16													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-7 Dealing With Strong Torreandos &amp; Recovering Lapel Guard													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:27													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-8 Using Baby Hooks &amp; the Pancake Philosophy													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:28													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-9 Using Lapels to Escape from Double Unders With Your Foot in the Collar													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:14													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-10 Overhook Wrench													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:14													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-11 Underhook Wrench													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														02:29													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														3-12 How to Escape When You`re Fully Stacked													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:18													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																			</ul>
								</div>
							</div>
																	</div>"""
chapter4 = """<div class="tutor-accordion-item">
						<h4 class="tutor-accordion-item-header is-active">
							Chapter 4: Worm Guard													</h4>
			
																			<div class="tutor-accordion-item-body" style="">
								<div class="tutor-accordion-item-body-content">
									<ul class="tutor-course-content-list">
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														<a href="https://jiujitsux.com/courses/keenans-lapel-encyclopedia/lesson/4-1-basic-worm-guard-entry-2/"><span class="lesson-preview-title">4-1 Basic Worm Guard Entry</span></a>													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														08:27													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-eye-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-2 Entry from Single-Leg X													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														02:32													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-3 Lapel Lasso Entry													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:05													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-4 Control Points, Balance and Weaknesses													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														08:26													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-5 The Very First Worm Guard Sweep Ever													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														06:23													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-6 Worm Guard Scissor Sweep													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														03:24													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-7 Emergency Exiting the Worm &amp; Becoming a Wrestler													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														05:35													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-8 Deep De La Worm Back Take													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														06:45													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-9 Fancy Spinning Sh*t													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														04:22													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-10 Using Shin to Shin to Secure Knee Over Knee													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														06:33													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																																<li class="tutor-course-content-list-item">
												<div class="tutor-d-flex tutor-align-center">
													<span class="tutor-course-content-list-item-icon tutor-icon-brand-youtube-bold tutor-mr-12"></span>
													<h5 class="tutor-course-content-list-item-title">
														4-11 Dealing With Spazzy Guys Who Do Ninja Rolls and Cartwheels													</h5>
												</div>
												
												<div>
													<span class="tutor-course-content-list-item-duration tutor-fs-7 tutor-color-muted">
														04:40													</span>
													<span class="tutor-course-content-list-item-status tutor-icon-lock-line tutor-color-muted tutor-ml-20" area-hidden="true"></span>
												</div>
											</li>
																			</ul>
								</div>
							</div>
																	</div>"""



if __name__=='__main__':
    soup = BeautifulSoup(chapter4, 'html.parser')
    print(soup.prettify())
